import logging

import environ

conf = {
    'bootstrap.servers': 'mybroker.com',
    'group.id': 'mygroup',
    'auto.offset.reset': 'latest',

    'security.protocol': 'sasl_ssl',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': '',
    'sasl.password': ''
}
logger = logging.getLogger(__name__)
env = environ.FileAwareEnv()


class KafkaConfig:

    def __init__(self):
        self.ORGANISATION_TOPIC = env('ILS_EVENT_API_KAFKA_ORGANISATION_TOPIC')

    def get_consumer_configuration(self):
        dic = self._base_configuration()
        dic['group.id'] = env('ILS_EVENT_API_KAFKA_GROUP_ID')
        dic['auto.offset.reset'] = 'end'
        return dic

    @staticmethod
    def _base_configuration():
        return {
            'bootstrap.servers': env('ILS_EVENT_API_KAFKA_BOOTSTRAP_SERVERS'),
            'security.protocol': 'sasl_ssl',
            'sasl.mechanisms': 'PLAIN',
            'sasl.username': env('ILS_EVENT_API_KAFKA_USER'),
            'sasl.password': env('ILS_EVENT_API_KAFKA_PASSWORD'),
            'enable.ssl.certificate.verification': env('ILS_EVENT_API_KAFKA_DISABLE_CERTIFICATE_VERIFICATION',
                                                       default=False)
        }
