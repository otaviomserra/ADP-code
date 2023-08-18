import logging
import signal
from multiprocessing import Lock

from confluent_kafka import Consumer, KafkaException

from event.utils.config import KafkaConfig


class CCKafkaMessage:

    def __init__(self, topic, offset, value) -> None:
        self._topic = topic
        self._offset = offset
        self._value = value

    def topic(self):
        return self._topic

    def offset(self):
        return self._offset

    def value(self):
        return self._value


class IlsEventConsumer:

    def __init__(self, message_queue):
        self.KEEP_RUNNING = True
        signal.signal(signal.SIGINT, self._stop_from_signal)
        signal.signal(signal.SIGTERM, self._stop_from_signal)

        self.message_queue = message_queue

        self._lock = Lock()

        self._logger = logging.getLogger(__name__)

        self._kafka_config = KafkaConfig()

        consumer_config = self._kafka_config.get_consumer_configuration()
        self.consumer = Consumer(consumer_config)

    def _log_received_message(self, topic: str, message: bytes):
        msg = message.decode("utf-8")

        self._logger.debug(f"KAFKA | RECEIVED | [topic={topic}] | [content={msg}]")

    def start_consumer(self):
        try:
            self.consumer.subscribe([self._kafka_config.ORGANISATION_TOPIC])
        except KafkaException as error:
            self._logger.error(f"Unable to subscribe to topics: {str(error)}")
            self._logger.warning("Kafka consumption aborted due to issues while subscribing to topics.")
            self.KEEP_RUNNING = False

        if self.KEEP_RUNNING:
            self._logger.info("Starting consumer...")

        while self.KEEP_RUNNING:
            try:
                while self.KEEP_RUNNING:
                    msg = self.consumer.poll(1.0)

                    if msg is None:
                        continue
                    if msg.error():
                        self._logger.error(f"Consumer error: {msg.error()}")
                        continue

                    self._log_received_message(msg.topic(), msg.value())

                    kafka_message = CCKafkaMessage(msg.topic(), msg.offset(), msg.value())
                    self.message_queue.put(kafka_message)

            except KafkaException as error:
                self._logger.error("Error while consuming from kafka: %s", str(error))

    def _stop_from_signal(self, sig, frame):
        self._logger.info(f"Shutting down signal '{signal.Signals(sig).name}' received, starting to stop consumer!")
        self._stop()

    def _stop(self):
        self._lock.acquire()

        self._logger.info("Ordering consumer to stop!")
        self.KEEP_RUNNING = False

        self._logger.debug("Warning Event Processors to stop!")
        self.message_queue.put("stop")

        self._logger.debug("Closing consumer!")
        self.consumer.unsubscribe()
        self.consumer.close()
        self._logger.debug("Consumer has been shutdown!")
        del self.consumer

        self._lock.release()
        del self._lock
