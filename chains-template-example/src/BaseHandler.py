import logging
import json
import sys

from IHandler import IHandler


logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)



class BaseHandler(IHandler):

    def __init__(self):
        self.next_handler = None
        self.logger = logger

    def save_to_file(self, file_input, file_output):
        try:
            with open(file_input, 'r') as f:
                content = f.readlines()
        except FileNotFoundError:
            self.logger.info('Input file doesnt exists')
            return

        try:
            with open(file_output, 'a') as f:
                for i in content:
                    f.write('Used handler: {0} '.format(self.__class__.__name__) + json.dumps(i) + '\n')
        except FileNotFoundError:
            self.logger.info('Output directory doesnt exists')
            return

    def set_next(self, handler):
        self.next_handler = handler

    def handle(self):
        if self.next_handler:
            self.next_handler.handle()

    def _log_handle(self, value: str):
        self.logger.info('Handler {0} handle file {1}'.format(self.__class__.__name__, value))
