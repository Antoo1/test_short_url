import logging.config

from short_url.app.config import config

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': (
                '%(levelname)s::%(asctime)s:%(name)s.%(funcName)s:\n%(message)s\n'
            ),
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        '': {
            'level': 'ERROR',
            'handlers': ['console'],
        },
        config.APP_NAME: {
            'level': config.LOG_LEVEL,
            'handlers': ['console'],
            'propagate': False
        },
    },
    'disable_existing_loggers': False,
}


def init_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
