import logging
import structlog
from dotenv import load_dotenv
import os

def configure_logging() -> structlog.BoundLogger:
    load_dotenv()
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(level=log_level, format="%(message)s")
    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(getattr(logging, log_level)),
        processors=[structlog.processors.JSONRenderer()]
    )
    return structlog.get_logger()
