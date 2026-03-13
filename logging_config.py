import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger():
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(
        "logs/trading.log",
        maxBytes=1_000_000,
        backupCount=3
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger