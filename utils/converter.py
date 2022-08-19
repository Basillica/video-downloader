import subprocess
from pathlib import Path


def convert_video_to_audio_ffmpeg(home_path: str, video_file: str, filename: str, output_ext: str = "mp3") -> None:
    """Converts video to audio directly using `ffmpeg` command
    with the help of subprocess module"""
    subprocess.call(["ffmpeg", "-y", "-i", f"{home_path}/{video_file}", f"{home_path}/{filename}.{output_ext}"], 
        stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
    )

    path = Path(f"{home_path}/{filename}.{output_ext}")
    if path.is_file():
        delete_video(f"{home_path}/{video_file}")
    else:
        print("could not confirm that file is in folder")
        pass


def delete_video(file_path: str):
    file_to_rem = Path(file_path)
    file_to_rem.unlink()