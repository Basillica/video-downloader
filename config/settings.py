from dataclasses import dataclass
from typing import TypeVar, Dict, Any, Type
from config.logger import Logger as CustomLogger
from logging import Logger
import os

ConfigClass = TypeVar('ConfigClass', bound='Config')

LOG_FILE = "logfile.log"
#create a new file for every new experiment
if (os.path.exists(LOG_FILE)):
    os.remove(LOG_FILE)


setup = {
    "VERSION": 1,
    "STAGE": "DEV",
    "logger": CustomLogger(logger_name="Video-Downloader", log_file=LOG_FILE).get_logger(),
}

@dataclass
class Config:
    VERSION: int
    STAGE: str
    logger: Logger

    @classmethod
    def from_config(cls: Type[ConfigClass], raw_config: Dict[str, Any]) -> ConfigClass:
        return cls(**raw_config)

def configure(stage=str) -> Config:
    if stage not in ['DEV', 'PROD']: stage = 'DEV'
    return Config.from_config(setup)
