from .logging_config import configure_logging

logger = configure_logging()


def main() -> None:
    logger.info("mcp initialized")


if __name__ == "__main__":
    main()
