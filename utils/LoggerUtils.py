import logging
import logging.config
from pathlib import Path


class LoggerUtils:
    path = Path("resources/logger_config.conf")
    logging.config.fileConfig(fname=path.absolute(),
                              disable_existing_loggers=False)

    @staticmethod
    def info(message):
        return logging.getLogger(__name__).info(message)

    @staticmethod
    def debug(message):
        return logging.getLogger(__name__).debug(message)

    @staticmethod
    def error(message):
        return logging.getLogger(__name__).error(message)


