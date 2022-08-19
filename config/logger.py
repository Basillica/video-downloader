from dataclasses import dataclass
import logging
from typing import List


@dataclass
class Logger(object):
    """Returns a customized Logger class instance.
    Example:
        logger = Logger.get_logger(logger_name='test-logger', log_file= "log-file.log")

    Args:
        object (_type_): _description_
        logger_name (str): The name of the logger
        log_level (str): The log level of the logger. Defaults to INFO if NONE or WRONG INPUT is provided
        log_file (str): Optional file name for log input. If provided, logs are also written to this file.
            If not created, it is created on the fly.

    Returns:
        logging.Logger: An instance of the logger class
    """
    logger_name: str
    log_level: str = 'INFO'
    log_file: str = None
    
    def get_logger(self) -> logging.Logger:
        
        """Method for creating a custom logger

        Returns:
            logging.Logger: The customized logger class
        """        
        log = logging.getLogger(self.logger_name)
        log.setLevel(level=self._get_log_level())
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s => %(message)s')
        if self.log_file:
                file_handler = logging.FileHandler(self.log_file)
                file_handler.setLevel(level=self._get_log_level())
                file_handler.setFormatter(formatter)

        channel = logging.StreamHandler()
        channel.setLevel(level=self._get_log_level())
        channel.setFormatter(formatter)
        if self.log_file:
            log.addHandler(file_handler)

        log.addHandler(channel)
        return log

    @classmethod
    def _get_log_level(self) -> int:
        """Class method for retrieving the right log level

        Returns:
            int: The log level  of the logger
        """
        log_levels = {
            "CRITICAL":  logging.CRITICAL,
            "FATAL":  logging.CRITICAL,
            "ERROR": logging.ERROR,
            "WARNING": logging.WARNING,
            "WARN": logging.WARNING,
            "INFO": logging.INFO,
            "DEBUG": logging.DEBUG,
            "NOTSET": logging.INFO,
        }
        return log_levels.get(self.log_level, logging.INFO)

    
def fetch_logs(log_file: str, chunk_size: int = 100) -> List[str]:
    def split_into_batches(lines, chunk_size):
        for i in range(0, len(lines), chunk_size):
            yield lines[i:i + chunk_size]

    with open(log_file) as f:
        lines = [line.rstrip() for line in f]
    if len(lines) > chunk_size:
        lines
        return merge_logs_into_string(list(split_into_batches(lines, chunk_size)))
    return merge_logs_into_string([lines])


def merge_logs_into_string(logs: List[str]):
    return ['\n'.join(map(str, log)) for log in logs]
