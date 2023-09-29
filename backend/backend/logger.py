import functools
import logging
from logging.handlers import RotatingFileHandler
from sys import stdout

from django.conf import settings


def logger_factory(name: str) -> logging.Logger:
    """Генерирует преднастроенный логгер по заданному имени."""
    logger = logging.getLogger(name)

    logger.setLevel(
        logging.DEBUG if settings.LOGGING['debug'] else logging.CRITICAL
    )

    c_handler = logging.StreamHandler(stdout)
    f_handler = RotatingFileHandler(filename=settings.LOGGING['log_file'],
                                    maxBytes=10**6,
                                    backupCount=5,
                                    encoding='UTF-8')

    formatter = logging.Formatter(fmt=settings.LOGGING['log_format'],
                                  datefmt=settings.LOGGING['dt_format'])
    c_handler.setFormatter(formatter)
    f_handler.setFormatter(formatter)

    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger


def log_exceptions(logger: logging.Logger):
    """Декоратор для логгирования ошибок в log-файл"""
    def wrap_func(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if settings.DEBUG:
                if kwargs.get('state'):
                    state = kwargs["state"]
                    state_data = state.get_data()
                    logger.info(f'state={state.get_state()}')
                    logger.info(f'data={list(state_data.keys())}')
                logger.info(f'handled by {func.__name__}')
            try:
                return func(*args, **kwargs)
            except Exception as exception:  # noqa: B902
                logger.exception(f'Исключение в функции {func.__name__}')
                raise

        return wrapper

    return wrap_func
