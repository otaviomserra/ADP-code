from multiprocessing import Queue
from pprint import pformat

import environ

from core.ils.client import OperationsApi, SetLightOperationBody, DefaultResponse, CarrierApi, KanbanControlCycleApi
from core.ils.client.rest import ApiException
from core.ils.external.organisation_event_pb2 import OrganisationEvent
from event.utils.events_processor import EventProcessor
from utils.ils_api_client import get_client
from utils.message import message_deserializer
from utils.token import IlsApiTokenRefresher

env = environ.FileAwareEnv()


class OrganisationEventProcessor(EventProcessor):

    def __init__(self, queue: Queue, kafka_config, token_refresher: IlsApiTokenRefresher, *args, **kwargs):
        super(OrganisationEventProcessor, self).__init__(queue, kafka_config, *args, **kwargs)
        self._token_refresher = token_refresher

    def _handle_message(self, message):
        logger = self._logger

        # deserialize the message payload
        msg = message_deserializer(message.value())

        if msg is None:
            logger.warning("Ignoring message since deserialization failed.")
            return

        body_case = msg.body.WhichOneof('body')

        logger.debug(f'handling a {body_case} event...')

        if body_case == 'action':
            action = msg.body.action

            if action.WhichOneof('body') == 'carrier':
                self._handle_carrier_event(action.carrier)
        elif body_case == 'identification':
            identifier_changed: OrganisationEvent.Identification.IdentifierChanged = \
                msg.body.identification.identifier_changed

            # TODO - this event payload will need to be modified in order to properly identify it!
            if identifier_changed is not None and str(identifier_changed.identifier.code) != '':
                self._handle_identification_changed(identifier_changed)

    def _handle_carrier_event(self, carrier: OrganisationEvent.Action.Carrier):
        logger = self._logger

        # connection between lanes and next control cycle
        lanes = ["S001.M003.02.01",
                 "S001.M003.02.02",
                 "S001.M005.01.03",
                 "S001.M007.01.01",
                 "S001.M007.01.02",
                 "S001.M007.01.03",
                 "S001.M004.01.02",
                 "S001.M007.01.04",
                 "S001.M007.02.01",
                 "S001.M007.02.02",
                 "S001.M007.02.03",
                 "S001.M007.02.04",
                 "S001.M004.01.01",
                 "S001.M004.02.01",
                 "S001.M004.02.02",
                 "S001.M004.03.01",
                 "S001.M004.03.02",
                 "S001.M004.04.01",
                 "S001.M004.04.02",
                 "S001.M005.03.03"]
        pick_lanes = ["S001.M003.02.01",
                      "S001.M003.02.02",
                      "S001.M005.01.03",
                      "S001.M007.01.01",
                      "S001.M007.01.02",
                      "S001.M007.01.03",
                      "S001.M004.01.02",
                      "S001.M007.01.04",
                      "S001.M007.02.01",
                      "S001.M007.02.02",
                      "S001.M007.02.03",
                      "S001.M007.02.04",
                      "S001.M004.01.01",
                      "S001.M004.02.01",
                      "S001.M004.02.02",
                      "S001.M004.03.01",
                      "S001.M004.03.02",
                      "S001.M004.04.01",
                      "S001.M004.04.02",
                      "S001.M005.03.03"]

        lane_ids = ["aed94e2e-d66e-468a-bcf0-d122fdbc0b10",
                    "d8034fa3-664d-4e32-ab2d-6e0abf6e23d4",
                    "aadf95aa-c11e-41a5-adf3-377b540000ab",
                    "c63c5b2c-b368-4f15-92ff-812733582ba8",
                    "e16d6f63-ffd6-4a1c-83b6-e1ce18dc17a8",
                    "ffc280cd-13a8-49e9-a06a-1281e826645d",
                    "8d20ae37-d762-4d4a-935a-2d07fec2af7e",
                    "417aec52-81db-459b-9259-21699851a9d1",
                    "72638c2d-39fe-426f-aa6c-ba155236f1d0",
                    "266b32ef-d2e6-4b6a-979d-ab161cd5b83a",
                    "04e45f88-44aa-41b1-b5d9-8183bf3fa935",
                    "bd4e17b4-44a3-40f5-945a-ccf568820eae",
                    "7a5dc1a2-d105-40ec-bcda-5f7c7cb2261b",
                    "2f391f1c-0488-4b21-a215-fe77978d3886",
                    "5a899a44-ea75-4358-a20b-0b338212c1fa",
                    "12b892e8-63b8-4927-8607-a7169e78a9f5",
                    "cb043b49-96b7-4f6e-8374-3bb8bbb15a32",
                    "3fb5394e-4828-44bd-9732-eeb572cc1c10",
                    "1a6acfef-0beb-4115-80c2-9c9cf02c6208",
                    "396e2360-6fec-4e18-9072-8b4e2c6c90fe"]

        control_cycle_ids = ["51c97b7a-e490-4430-87e7-4d9a78046b44",
                             "15c5e6f6-a406-4f02-bac3-0521d51f86fc",
                             "54c4b38d-174a-409f-9d86-5a98bcb464ee",
                             "538a71e2-99b9-4e5d-8fab-bdcde4868f0d",
                             "e1dc3046-93f5-48ed-b2cf-bd605e3eaff7",
                             "50cb3ac3-e7b4-4db1-9690-9c89ff62ef97",
                             "05925966-7932-4e7f-91ee-034b21e2ef5b",
                             "5624ba3f-327e-4bd7-b021-81a9ac08f6cc",
                             "f1749739-f4ac-4206-af28-5bc7b3322484",
                             "9adf1dbf-58ad-4ba1-bd29-22d25e22c53c",
                             "a3ff8527-2582-474f-90b3-0abb7ae0c021",
                             "082c2b14-e019-4fb0-9c88-200fa424aaa3",
                             "f7362cb4-d4eb-4f83-a140-456141e96b10",
                             "01ec2ee7-38db-4a9f-8e1c-5db90301b09e",
                             "eee9e685-28b1-4f25-8cb9-67af433f7cc5",
                             "1c83b022-c500-4b81-bef5-9b33b36127bb",
                             "352f5c2e-2a62-43b6-b8a4-5344c9d30c32",
                             "89e106ac-ce69-4d66-9e41-f81e2a014320",
                             "420d411a-509a-490d-bc26-9cfd51330ea3",
                             "41ffe350-3606-46e6-bc64-0655e6ae959a"]

        emptie_lanes = ["S001.M006.03.01",
                        "S001.M006.03.03",
                        "S001.M006.03.05"]
        emptie_lanes_ids = ["b01bbb45-f148-4a3a-b245-c41be7b22564",
                            "721d55ea-f3cb-4a14-8dd4-4a47264865aa",
                            "74f4bb5e-061e-4b64-860b-2b6be305db35"]

        # for the Linked Kanban Control Cycles we only care about the Pick events
        from core.ils.external.types_pb2 import CARRIER_ACTION_PICK
        from core.ils.external.types_pb2 import CARRIER_ACTION_PUT

        if carrier.carrier_action_type == CARRIER_ACTION_PUT:
            empties_lane_adress = carrier.lane_address
            try:
                index_empties = emptie_lanes.index(empties_lane_adress)
            except:
                index_empties = -1
            if index_empties == -1:
                return
            else:
                emptie_lanes_id = emptie_lanes_ids[index_empties]
                self._signal_linked_lane(emptie_lanes_id, 1)

        if carrier.carrier_action_type == CARRIER_ACTION_PICK:

            lane_address = carrier.lane_address
            target_lane_id = self._get_linked_lane(lane_address)[0]

            laneposition = self._get_linked_lane(lane_address)[1]
            # if target_lane_id is None:
            #     return

            logger.info(f'signal linked lane {lane_address} -> {target_lane_id}')
            self._signal_linked_lane(target_lane_id, laneposition)

            # Kanbanzykluswechsel
            carrier_id = carrier.carrier_id
            try:
                index = lanes.index(lane_address)
            except:
                index = -1

            new_control_cycle_id = control_cycle_ids[index]
            print(index)
            print("neuer CC:", new_control_cycle_id)

            self._dissociate_card_from_carrier(carrier_id)
            self._assign_card_to_carrier(carrier_id, new_control_cycle_id)

            try:
                stop_blink_index = pick_lanes.index(lane_address)
            except:
                stop_blink_index = -1

            if stop_blink_index == -1:
                return
            else:
                stop_blink_lane_id = lane_ids[stop_blink_index]
                self._signal_linked_lane(stop_blink_lane_id, laneposition=3)
                self._signal_linked_lane(stop_blink_lane_id, laneposition=4)

        # if carrier.carrier_action_type == CARRIER_ACTION_PUT
        #     lane_address1 = [S001.M006.03.01]

    def _handle_identification_changed(self,
                                       identification_changed: OrganisationEvent.Identification.IdentifierChanged):
        logger = self._logger

        logger.debug(f'identification changed {identification_changed.identifier.code} ->'
                     f' {identification_changed.identifier.metadata}')

    @staticmethod
    def _get_linked_lane(source_address):
        # TODO improve me
        LINKED_KCC_SOURCE_LANE_ADDRESS = ["S001.M004.01.02",
                                          "S001.M006.02.04",
                                          "S001.M006.02.05",
                                          "S001.M006.01.05",
                                          "S001.M006.01.04",
                                          "S001.M006.02.03",
                                          "S001.M006.01.03",
                                          "S001.M006.01.02",
                                          "S001.M006.02.02",
                                          "S001.M006.02.01",
                                          "S001.M006.01.01",
                                          "S001.M004.01.01",
                                          "S001.M004.02.01",
                                          "S001.M004.02.02",
                                          "S001.M004.03.01",
                                          "S001.M004.03.02",
                                          "S001.M004.04.01",
                                          "S001.M004.04.02"]
        LINKED_KCC_TARGET_LANE_ID = ["c63c5b2c-b368-4f15-92ff-812733582ba8",
                                     "aadf95aa-c11e-41a5-adf3-377b540000ab",
                                     "8d20ae37-d762-4d4a-935a-2d07fec2af7e",
                                     "7a5dc1a2-d105-40ec-bcda-5f7c7cb2261b",
                                     "396e2360-6fec-4e18-9072-8b4e2c6c90fe",
                                     "cb043b49-96b7-4f6e-8374-3bb8bbb15a32",
                                     "12b892e8-63b8-4927-8607-a7169e78a9f5",
                                     "3fb5394e-4828-44bd-9732-eeb572cc1c10",
                                     "1a6acfef-0beb-4115-80c2-9c9cf02c6208",
                                     "5a899a44-ea75-4358-a20b-0b338212c1fa",
                                     "2f391f1c-0488-4b21-a215-fe77978d3886",
                                     "ffc280cd-13a8-49e9-a06a-1281e826645d",
                                     "417aec52-81db-459b-9259-21699851a9d1",
                                     "e16d6f63-ffd6-4a1c-83b6-e1ce18dc17a8",
                                     "04e45f88-44aa-41b1-b5d9-8183bf3fa935",
                                     "72638c2d-39fe-426f-aa6c-ba155236f1d0",
                                     "bd4e17b4-44a3-40f5-945a-ccf568820eae",
                                     "266b32ef-d2e6-4b6a-979d-ab161cd5b83a"]
        x = [1,
             2,
             2,
             2,
             2,
             2,
             2,
             2,
             2,
             2,
             2,
             1,
             1,
             1,
             1,
             1,
             1,
             1]
        # 1 means the target lane is in the central warehouse, 2 the lane is in the middle supermarket

        # Maybe you can build some dictionary / lookup table
        # and associate lane addresses with target Lane Ids
        #
        # This version here relies on two environment variables for demonstration purposes
        # the idea is that we can have this code working with a single use case on any environment
        # it is clearly limited.
        #
        # Please improve it as you see fit.
        try:
            index = LINKED_KCC_SOURCE_LANE_ADDRESS.index(source_address)
        except:
            index = -1

        if source_address == LINKED_KCC_SOURCE_LANE_ADDRESS[index]:
            return LINKED_KCC_TARGET_LANE_ID[index], x[index]
        return LINKED_KCC_TARGET_LANE_ID[index], x[index]

    def _signal_linked_lane(self, lane_id, laneposition):
        logger = self._logger

        api_client = get_client(self._token_refresher)

        operations_instance = OperationsApi(api_client)
        if laneposition == 1:
            try:
                api_response: DefaultResponse = operations_instance.request_set_light(
                    SetLightOperationBody(color="BLUE", blink=True, duration=1000, side="PRIMARY"),
                    lane_ids=[lane_id])

                logger.info(pformat(api_response))
            except ApiException as e:
                logger.error(f'Exception when calling ILS API: {e}')
            except Exception as e:
                logger.debug(f'Exception when calling ILS API: {e}')

        if laneposition == 2:
            try:
                api_response: DefaultResponse = operations_instance.request_set_light(
                    SetLightOperationBody(color="BLUE", blink=True, duration=1000, side="SECONDARY"),
                    lane_ids=[lane_id])

                logger.info(pformat(api_response))
            except ApiException as e:
                logger.error(f'Exception when calling ILS API: {e}')
            except Exception as e:
                logger.debug(f'Exception when calling ILS API: {e}')

        if laneposition == 3:
            try:
                api_response: DefaultResponse = operations_instance.request_set_light(
                    SetLightOperationBody(color="GREEN", blink=True, duration=1, side="PRIMARY"),
                    lane_ids=[lane_id])
            except ApiException as e:
                logger.error(f'Exception when calling ILS API: {e}')
            except Exception as e:
                logger.debug(f'Exception when calling ILS API: {e}')

        if laneposition == 4:
            try:
                api_response: DefaultResponse = operations_instance.request_set_light(
                    SetLightOperationBody(color="GREEN", blink=True, duration=1, side="SECONDARY"),
                    lane_ids=[lane_id])

                logger.info(pformat(api_response))
            except ApiException as e:
                logger.error(f'Exception when calling ILS API: {e}')
            except Exception as e:
                logger.debug(f'Exception when calling ILS API: {e}')

    def _dissociate_card_from_carrier(self, carrier_id):
        logger = self._logger

        api_client = get_client(self._token_refresher)

        operations_instance = CarrierApi(api_client)
        try:
            api_response: DefaultResponse = operations_instance.dissociate_card_from_carrier(
                carrier_id=carrier_id)
            logger.info(pformat(api_response))
        except ApiException as e:
            logger.error(f'Exception when calling ILS API: {e}')
        except Exception as e:
            logger.debug(f'Exception when calling ILS API: {e}')

    def _assign_card_to_carrier(self, carrier_id, control_cycle_id):
        logger = self._logger

        api_client = get_client(self._token_refresher)

        operations_instance = KanbanControlCycleApi(api_client)
        try:
            api_response: DefaultResponse = operations_instance.assign_kanban_card_to_carrier(
                control_cycle_id=control_cycle_id, carrier_id=carrier_id)
            logger.info(pformat(api_response))
        except ApiException as e:
            logger.error(f'Exception when calling ILS API: {e}')
        except Exception as e:
            logger.debug(f'Exception when calling ILS API: {e}')