from pytube import YouTube
from config import Config
from pathlib import Path
from utils import convert_video_to_audio_ffmpeg


def download(config: Config, output_path: str, link: str, file_type: str, path: str = None) -> None:
    path = f"{Path.home()}/Desktop/downloads"
    # print(*Path(Path.home()).iterdir(), sep="\n")
    if file_type == "mp4":
        config.logger.info(f"Downloading file in mp4 format ...")
        yt = YouTube(f"http://youtube.com/watch?v={link}")
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=path, filename=f"{output_path}.{file_type}")
        config.logger.info(f"Video download completed")
        config.logger.info(f"Converting video to audio ...")
        convert_video_to_audio_ffmpeg(path, f"{output_path}.{file_type}", output_path)
        config.logger.info(f"Audio convert completed!")


    elif file_type == "3gpp":
        config.logger.info(f"Downloading file in 3gpp format")
        YouTube(f'https://youtu.be/{link}').streams.first().download(output_path="~/Desktop", filename=f"{output_path}.{file_type}")
    else:
        config.logger.error(f"Wrong file extension format provided. Provided value: {file_type}")
        raise Exception(f"Wrong file extension format provided. Provided value: {file_type}")