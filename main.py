from config import run, configure
from scr import Downloader

custom_video_downloader = Downloader()

@custom_video_downloader.app.command(name='youtube', help="Method to download a video from a youtube link", short_help="Download youtube video")
def download_video(
        stage = custom_video_downloader.get_stage_options(),
        link = custom_video_downloader.get_link_options(),
        file_type = custom_video_downloader.get_file_type_options(),
        output = custom_video_downloader.get_output_options(),
    ):
    config = configure(stage)
    run(
        config=config, command="youtube", 
        link=link, output_path=output, file_type=file_type
    )
    config.logger.info("Task completed")


@custom_video_downloader.app.command(name='instagram', help="Method to download a video from an instagram link", short_help="Download instagram video")
def download_video(
        stage = custom_video_downloader.get_stage_options(),
        link = custom_video_downloader.get_link_options(),
        file_type = custom_video_downloader.get_file_type_options(),
        output = custom_video_downloader.get_output_options(),
    ):
    config = configure(stage)
    run(
        config=config, command="instagram", 
        link=link, output_path=output, file_type=file_type
    )
    config.logger.info("Task completed")


@custom_video_downloader.app.command(name='facebook', help="Method to download a video from a facebookl link", short_help="Download facebook video")
def download_video(
        stage = custom_video_downloader.get_stage_options(),
        link = custom_video_downloader.get_link_options(),
        file_type = custom_video_downloader.get_file_type_options(),
        output = custom_video_downloader.get_output_options(),
    ):
    config = configure(stage)
    run(
        config=config, command="facebook", 
        link=link, output_path=output, file_type=file_type
    )
    config.logger.info("Task completed")


if __name__ == "__main__":
    custom_video_downloader.app()
