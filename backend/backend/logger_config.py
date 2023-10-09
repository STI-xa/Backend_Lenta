import logging


class LoggingSettings:
    def __init__(self, log_file, log_format, dt_format, debug):
        self.log_file = log_file
        self.log_format = log_format
        self.dt_format = dt_format
        self.debug = debug

    def init_global_logging_level(self):
        logging.basicConfig(
            level=logging.DEBUG if self.debug else logging.CRITICAL
        )
