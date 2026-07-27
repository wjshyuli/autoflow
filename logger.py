from loguru import logger


logger.add(
    "autoflow.log",
    rotation="10 MB",
    retention="30 days",
    encoding="utf-8"
)