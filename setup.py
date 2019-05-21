import os
import json
import logging.config

class Setup:
    def get_directories(self):
        config_file = open("/Users/ajayraj/Documents/Xcode-VS-Adapt/config.json", "r")
        config = json.load(config_file)
        config_file.close()
        directories = (
                            config["file-directories"]["Xcode"],
                            config["file-directories"]["Visual-Studio"],
                            config["git-directories"]["Visual-Studio"]
        )
        return directories


    def set_dictConfig(self):
        LOGGING = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "%(asctime)s %(levelname)s %(name)s %(message)s"
                },
            },
            "handlers": {
                "copy_handler": {
                        "class": "logging.FileHandler",
                        "formatter": "default",
                        "filename": "copier.log"
                }
            },
            "loggers": {
                "copy_logger": {
                    "handlers": ["copy_handler"],
                    "level": "INFO",
                }

            }
        }
        logging.config.dictConfig(LOGGING)