import logging
from multiprocessing import Process, Queue
from queue import Empty


class EventProcessor(Process):
    def __init__(self, queue: Queue, kafka_config, *args, **kwargs):
        super(EventProcessor, self).__init__(*args, **kwargs)
        self._logger = logging.getLogger(__name__)

        self.queue = queue
        self.kwargs = kwargs
        self.kafka_config = kafka_config

    def run(self):
        self._logger.info(f"{self.__class__.__name__} Running!")

        while True:
            try:

                message = self.queue.get()

                if type(message) is str:
                    self._logger.info(f"{self.__class__.__name__} received order to stop!")
                    break

                self._handle_message(message)

            except Empty:
                pass
            except KeyboardInterrupt:
                pass

        self._logger.info(
            f"All messages in {self.__class__.__name__} processing queue have been processed. Shutting down...")

        del self.kafka_producer
        self.queue.close()

        del self.queue

    def _handle_message(self, message):
        # OVERRIDE ME
        pass
