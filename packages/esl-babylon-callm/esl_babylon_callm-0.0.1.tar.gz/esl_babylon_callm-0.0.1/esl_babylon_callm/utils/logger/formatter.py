import logging


class Colors:
    DEBUG = '\033[36m'  # Cyan
    INFO = '\033[32m'  # Green
    WARNING = '\033[33m'  # Yellow
    ERROR = '\033[31m'  # Red
    CRITICAL = '\033[41m'  # Red background and white text
    RESET = '\033[0m'  # Reset color to default


class CustomFormatter(logging.Formatter):
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: f"{Colors.DEBUG};20m{format}{Colors.RESET}",
        logging.INFO: f"{Colors.INFO}{format}{Colors.RESET}",
        logging.WARNING: f"{Colors.WARNING}{format}{Colors.RESET}",
        logging.ERROR: f"{Colors.ERROR}{format}{Colors.RESET}",
        logging.CRITICAL: f"{Colors.CRITICAL}{format}{Colors.RESET}",
    }

    def format(self, record) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
