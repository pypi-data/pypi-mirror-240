import logging

from esl_babylon_callm.config import app_config
from esl_babylon_callm.utils.logger.formatter import CustomFormatter


def create_logger() -> logging.Logger:
    new_logger = logging.getLogger(app_config.app_name)
    numeric_level = getattr(logging, app_config.log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {app_config.log_level}")
    new_logger.setLevel(numeric_level)

    # create console handler with a higher log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(numeric_level)

    console_handler.setFormatter(CustomFormatter())

    new_logger.addHandler(console_handler)
    return new_logger


logger = create_logger()
