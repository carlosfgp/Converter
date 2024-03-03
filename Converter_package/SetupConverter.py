import os

from Logger_Converter import LoggerConverter


def setup_file_directory():
    current_directory = os.path.dirname(__file__)
    log = LoggerConverter.logger(__name__)

    directories = ["config", "tmp", os.path.join(os.path.expanduser("~"), "Runbooks")]

    for directory in directories:
        log.info(f"Setting up directory \"{directory}\" on directory... \"{current_directory}\"")

        path = os.path.join(current_directory, directory)
        try:
            if not os.path.exists(path):
                os.makedirs(os.path.join(current_directory, directory))
                log.info(f"{directory} directory created")
            else:
                log.info(f"{directory} directory already created")

        except FileNotFoundError as e:
            log.info(f"File not found: {e}")
