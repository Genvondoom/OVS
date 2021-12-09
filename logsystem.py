import logging


class Log:
    fileName = None
    logging.basicConfig(filename=f"test.log", level=logging.DEBUG)

    def message_log(self, message):
        logging.info(message)
