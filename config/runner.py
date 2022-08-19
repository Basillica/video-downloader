from .settings import Config
from sources import download


def run(config: Config, command: str, link: str, output_path: str, file_type: str, path: str = None):
    if command == "youtube":
        download(config=config, output_path=output_path, 
            link=link, file_type=file_type, path=path
        )
    elif command == "instagram":
        config.logger.info("Instagram command selected")
        pass
    elif command == "facebook":
        config.logger.info("Facebook command selected")
        pass
    else:
        config.logger.error("No valid command selected")
        pass