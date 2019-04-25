import logging
import logging.config


def config_logger(name):
    logging.config.dictConfig({
        "version": 1,

        "disable_existing_loggers": False,

        "formatters": {
            "simple": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
            # add formatters here.
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            },

            "info_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "simple",
                "filename": "info.log",
                "maxBytes": 41943040,
                "backupCount": 5,
                "encoding": "utf8"
            },
            "debug_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "filename": "debug.log",
                "maxBytes": 41943040,
                "backupCount": 5,
                "encoding": "utf8"
            },
            # add handlers here.
        },

        "loggers": {
            "debugger": {
                "level": "DEBUG",
                "handlers": ["console"],
                "propagate": False
            },
            "infologger": {
                "level": "INFO",
                "handlers": ["info_file_handler"]
            }
            # add loggers here
        },

        # default logger
        "root": {
                "level": "DEBUG",
                "handlers": ["console", "info_file_handler", "debug_file_handler"]
        },
    })
    return logging.getLogger(name)
