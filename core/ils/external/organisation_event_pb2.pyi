from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from core.ils.external import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrganisationEvent(_message.Message):
    __slots__ = ["body", "header"]
    class Action(_message.Message):
        __slots__ = ["carrier", "material"]
        class Carrier(_message.Message):
            __slots__ = ["carrier_action_type", "carrier_id", "current_count", "lane_address", "location_type"]
            CARRIER_ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
            CARRIER_ID_FIELD_NUMBER: _ClassVar[int]
            CURRENT_COUNT_FIELD_NUMBER: _ClassVar[int]
            LANE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
            carrier_action_type: _types_pb2.CarrierActionType
            carrier_id: str
            current_count: int
            lane_address: str
            location_type: _types_pb2.LocationType
            def __init__(self, lane_address: _Optional[str] = ..., carrier_action_type: _Optional[_Union[_types_pb2.CarrierActionType, str]] = ..., location_type: _Optional[_Union[_types_pb2.LocationType, str]] = ..., carrier_id: _Optional[str] = ..., current_count: _Optional[int] = ...) -> None: ...
        class Material(_message.Message):
            __slots__ = []
            def __init__(self) -> None: ...
        CARRIER_FIELD_NUMBER: _ClassVar[int]
        MATERIAL_FIELD_NUMBER: _ClassVar[int]
        carrier: OrganisationEvent.Action.Carrier
        material: OrganisationEvent.Action.Material
        def __init__(self, material: _Optional[_Union[OrganisationEvent.Action.Material, _Mapping]] = ..., carrier: _Optional[_Union[OrganisationEvent.Action.Carrier, _Mapping]] = ...) -> None: ...
    class Body(_message.Message):
        __slots__ = ["action", "identification", "trigger"]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_FIELD_NUMBER: _ClassVar[int]
        action: OrganisationEvent.Action
        identification: OrganisationEvent.Identification
        trigger: OrganisationEvent.Trigger
        def __init__(self, identification: _Optional[_Union[OrganisationEvent.Identification, _Mapping]] = ..., trigger: _Optional[_Union[OrganisationEvent.Trigger, _Mapping]] = ..., action: _Optional[_Union[OrganisationEvent.Action, _Mapping]] = ...) -> None: ...
    class Header(_message.Message):
        __slots__ = ["id", "organisation_id", "timestamp", "trace_id"]
        ID_FIELD_NUMBER: _ClassVar[int]
        ORGANISATION_ID_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        TRACE_ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        organisation_id: str
        timestamp: _timestamp_pb2.Timestamp
        trace_id: str
        def __init__(self, trace_id: _Optional[str] = ..., id: _Optional[str] = ..., organisation_id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Identification(_message.Message):
        __slots__ = ["identifier_changed", "lost", "present", "seen"]
        class Identifier(_message.Message):
            __slots__ = ["code", "enrichments", "id", "metadata"]
            class EnrichmentsEntry(_message.Message):
                __slots__ = ["key", "value"]
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: str
                def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
            class Metadata(_message.Message):
                __slots__ = ["rssi"]
                RSSI_FIELD_NUMBER: _ClassVar[int]
                rssi: int
                def __init__(self, rssi: _Optional[int] = ...) -> None: ...
            CODE_FIELD_NUMBER: _ClassVar[int]
            ENRICHMENTS_FIELD_NUMBER: _ClassVar[int]
            ID_FIELD_NUMBER: _ClassVar[int]
            METADATA_FIELD_NUMBER: _ClassVar[int]
            code: str
            enrichments: _containers.ScalarMap[str, str]
            id: str
            metadata: OrganisationEvent.Identification.Identifier.Metadata
            def __init__(self, id: _Optional[str] = ..., code: _Optional[str] = ..., metadata: _Optional[_Union[OrganisationEvent.Identification.Identifier.Metadata, _Mapping]] = ..., enrichments: _Optional[_Mapping[str, str]] = ...) -> None: ...
        class IdentifierChanged(_message.Message):
            __slots__ = ["identifier"]
            IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
            identifier: OrganisationEvent.Identification.Identifier
            def __init__(self, identifier: _Optional[_Union[OrganisationEvent.Identification.Identifier, _Mapping]] = ...) -> None: ...
        class Lost(_message.Message):
            __slots__ = ["identifier"]
            IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
            identifier: _containers.RepeatedCompositeFieldContainer[OrganisationEvent.Identification.Identifier]
            def __init__(self, identifier: _Optional[_Iterable[_Union[OrganisationEvent.Identification.Identifier, _Mapping]]] = ...) -> None: ...
        class Present(_message.Message):
            __slots__ = ["identifier"]
            IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
            identifier: _containers.RepeatedCompositeFieldContainer[OrganisationEvent.Identification.Identifier]
            def __init__(self, identifier: _Optional[_Iterable[_Union[OrganisationEvent.Identification.Identifier, _Mapping]]] = ...) -> None: ...
        class Seen(_message.Message):
            __slots__ = ["identifier"]
            IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
            identifier: _containers.RepeatedCompositeFieldContainer[OrganisationEvent.Identification.Identifier]
            def __init__(self, identifier: _Optional[_Iterable[_Union[OrganisationEvent.Identification.Identifier, _Mapping]]] = ...) -> None: ...
        IDENTIFIER_CHANGED_FIELD_NUMBER: _ClassVar[int]
        LOST_FIELD_NUMBER: _ClassVar[int]
        PRESENT_FIELD_NUMBER: _ClassVar[int]
        SEEN_FIELD_NUMBER: _ClassVar[int]
        identifier_changed: OrganisationEvent.Identification.IdentifierChanged
        lost: OrganisationEvent.Identification.Lost
        present: OrganisationEvent.Identification.Present
        seen: OrganisationEvent.Identification.Seen
        def __init__(self, seen: _Optional[_Union[OrganisationEvent.Identification.Seen, _Mapping]] = ..., lost: _Optional[_Union[OrganisationEvent.Identification.Lost, _Mapping]] = ..., present: _Optional[_Union[OrganisationEvent.Identification.Present, _Mapping]] = ..., identifier_changed: _Optional[_Union[OrganisationEvent.Identification.IdentifierChanged, _Mapping]] = ...) -> None: ...
    class Trigger(_message.Message):
        __slots__ = ["trigger_stock"]
        class TriggerStock(_message.Message):
            __slots__ = ["address", "lane_id", "state", "stock", "threshold", "trigger_name"]
            class TriggerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = []
            ABOVE: OrganisationEvent.Trigger.TriggerStock.TriggerState
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            BELOW: OrganisationEvent.Trigger.TriggerStock.TriggerState
            EQUAL: OrganisationEvent.Trigger.TriggerStock.TriggerState
            LANE_ID_FIELD_NUMBER: _ClassVar[int]
            STATE_FIELD_NUMBER: _ClassVar[int]
            STOCK_FIELD_NUMBER: _ClassVar[int]
            THRESHOLD_FIELD_NUMBER: _ClassVar[int]
            TRIGGER_NAME_FIELD_NUMBER: _ClassVar[int]
            UNKNOWN_STATE: OrganisationEvent.Trigger.TriggerStock.TriggerState
            address: str
            lane_id: str
            state: OrganisationEvent.Trigger.TriggerStock.TriggerState
            stock: int
            threshold: str
            trigger_name: str
            def __init__(self, lane_id: _Optional[str] = ..., trigger_name: _Optional[str] = ..., state: _Optional[_Union[OrganisationEvent.Trigger.TriggerStock.TriggerState, str]] = ..., stock: _Optional[int] = ..., threshold: _Optional[str] = ..., address: _Optional[str] = ...) -> None: ...
        TRIGGER_STOCK_FIELD_NUMBER: _ClassVar[int]
        trigger_stock: OrganisationEvent.Trigger.TriggerStock
        def __init__(self, trigger_stock: _Optional[_Union[OrganisationEvent.Trigger.TriggerStock, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    body: OrganisationEvent.Body
    header: OrganisationEvent.Header
    def __init__(self, header: _Optional[_Union[OrganisationEvent.Header, _Mapping]] = ..., body: _Optional[_Union[OrganisationEvent.Body, _Mapping]] = ...) -> None: ...
