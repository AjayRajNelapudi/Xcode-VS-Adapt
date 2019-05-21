import logging
import logging.config
import copier


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