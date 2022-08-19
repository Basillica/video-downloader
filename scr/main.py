import typer
from dataclasses import dataclass
import re
import random
import string


@dataclass
class Constants:
    app = typer.Typer()
    stage_tool_tip = typer.style("DEV or PROD", fg=typer.colors.BRIGHT_GREEN, bold=True, italic=True)
    provider_tool_tip = typer.style("YOUTUBE or INSTAGRAM OR FACEBOOK", fg=typer.colors.BRIGHT_GREEN, bold=True, italic=True)
    file_type_tool_tip = typer.style("3gpp or mp4. Default value is mp4", fg=typer.colors.BRIGHT_GREEN, bold=True, italic=True)
    url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

    def get_random_string(self, length: int = 10):
        combination = string.ascii_lowercase + string.ascii_uppercase + string.digits
        return ''.join(random.choice(combination) for i in range(length))
        

    def stage_callback(self, value: str) -> str:
        if not value:
            raise typer.BadParameter(f"AN env was not provided. Value should be either {self.stage_tool_tip}!")
        if value not in ["DEV", "PROD"]:
            raise typer.BadParameter(f"Invalid value for ENVIRONMENT provided. Value should be either {self.stage_tool_tip}!")
        return value.lower()

    def provider_callback(self, value: str) -> str:
        if not value:
            raise typer.BadParameter(f"A provider was not provided. Value should be either {self.provider_tool_tip}!")
        if value not in ["youtube", "facebook", "instagram"]:
            raise typer.BadParameter(f"Invalid value for the provider. Value should be either of {self.provider_tool_tip}!")
        return value.lower()
    
    def link_callback(self, value: str) -> str:
        if not value:
            raise typer.BadParameter(f"A link was not provided!")
        if not re.match(self.url_pattern, value):
            raise typer.BadParameter(f"Invalid url provided")
        m = re.search('v=(.+?)&', value)
        if not m:
            raise typer.BadParameter("The wrong url format was provided")
        return m.group(1)

    def file_type_callback(self, value: str) -> str:
        if not value:
            return "mp4"
        if value not in ["3gpp", "mp4"]:
            raise typer.BadParameter(f"Invalid url provided. Value should be either of {self.file_type_tool_tip}!")
        return value
    
    def output_callback(self, value: str) -> str:
        if not value:
            return self.get_random_string()
        return value

    def get_stage_options(self):
        return typer.Option(
                None,
                "--env", "-e",
                help="The environment for the test.",
                callback=self.stage_callback
            )
    
    def get_provider_options(self):
        return typer.Option(
                None,
                "--provider", "-p",
                help="The provider or the video source",
                callback=self.provider_callback
            )
        
    def get_link_options(self):
        return typer.Option(
                None,
                "--link", "-l",
                help="The link to the video source",
                callback=self.file_type_callback
            )

@dataclass
class Downloader(Constants):
    def get_stage_options(self):
        return typer.Option(
                None,
                "--env", "-e",
                help="The environment for the test.",
                callback=self.stage_callback
            )
    
    def get_provider_options(self):
        return typer.Option(
                None,
                "--provider", "-p",
                help="The provider or the video source",
                callback=self.provider_callback
            )
        
    def get_link_options(self):
        return typer.Option(
                None,
                "--link", "-l",
                help="The link to the video source",
                callback=self.link_callback
            )

    def get_file_type_options(self):
        return typer.Option(
                None,
                "--ext", "-x",
                help="The prefered file extension to be downloaded",
                callback=self.file_type_callback
            )
        
    def get_output_options(self):
        return typer.Option(
                None,
                "--output", "-o",
                help="The output name of the file to be saved",
                callback=self.output_callback
            )
