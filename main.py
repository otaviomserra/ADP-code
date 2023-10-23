import sys
import logging
from logging import config
from multiprocessing import Queue
from multiprocessing.context import Process
from typing import List
import csv

import environ

from event.organisation_event_processor import OrganisationEventProcessor
from event.utils.config import KafkaConfig
from event.utils.ils_event_consumer import IlsEventConsumer
from utils.token import IlsApiTokenRefresher
from datenverarbeitung.LogToCsv import *

# get time
import datetime
current_time = datetime.datetime.now()
#formatted_time = current_time.strftime('%Y-%m-%d %Hh-%Mm-%Ss')
formatted_time = current_time.strftime('%Y-%m-%d %Hh-%Mm')
#print(formatted_time)
# Save logs to logs folder
import os
if not os.path.exists('logs'):
   os.makedirs('logs')

log_path = f"datenverarbeitung\\raw_logs\\{formatted_time}.log"
fileHandler = (log_path + '.')[:-1]
#print(fileHandler)
#fileHandler = "logs/teste.log"

env = environ.FileAwareEnv()

log_level = env('LOG_LEVEL', default="DEBUG")

log_config = {
    "version": 1,
    "root": {
        "handlers": ["console", "file"],
        "level": log_level
    },
    "handlers": {
        "console": {
            "formatter": "std_out",
            "class": "logging.StreamHandler",
            "level": log_level,
            "stream": sys.stdout
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "mode": "a",
            "formatter": "std_out",
            "filename": fileHandler,
            "maxBytes": 1048576,
            "backupCount": 3,
        }
    },
    "formatters": {
        "std_out": {
            "format": '[%(asctime)s] "%(levelname)s" "%(module)s" "%(message)s"',
            "datefmt": "%d/%b/%Y %I:%M:%S"
        }
    },
}

config.dictConfig(log_config)

logger = logging.getLogger(__name__)


def start_application():
    logger.info("Starting application...")

    processes: List[Process] = []
    message_queue = Queue()

    consumer = IlsEventConsumer(message_queue)

    kafka_config = KafkaConfig()

    token_refresher = IlsApiTokenRefresher()

    logger.info(f'ils-api access: {token_refresher.get_token().is_valid()}')

    processes.append(
        OrganisationEventProcessor(message_queue, kafka_config=kafka_config, token_refresher=token_refresher))

    for process in processes:
        logger.debug(f"Starting process: '{process.name}'")
        process.start()

    consumer.start_consumer()

    for process in processes:
        logger.debug(f"Ending process: '{process.name}'")
        process.join()
        process.close()
        logger.info(f"Process {process.name} as fully stopped!")


if __name__ == '__main__':
    start_application()

    # log_filename = pfparadedarerrado
    # csv_filename = f"logs/{formatted_time}.csv"

    # event_handler = LogFileHandler(log_filename, csv_filename)
    # observer = Observer()
    # observer.schedule(event_handler, path=os.path.dirname(log_filename))
    # observer.start()

    # try:
    #     while True:
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     observer.stop()

    # observer.join()

# input_file_path =pfparadedarerrado

# output_file_path = f"logs/{formatted_time}.csv"

# with open(input_file_path, 'r') as text_file:
#     lines = text_file.readlines()

# data = [line.strip().split() for line in lines]
# data = [[item.strip('"') for item in row] for row in data]
# with open(output_file_path, 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerows(data)