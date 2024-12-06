import os
import logging
from dotenv import load_dotenv
from rich.logging import RichHandler

# Load environment variables
load_dotenv()


class Config:
    """Central configuration management"""

    # API Keys
    BUILTWITH_API_KEY = os.getenv("BUILTWITH_API_KEY")
    HUNTERIO_API_KEY = os.getenv("HUNTERIO_API_KEY")

    # Logging configuration
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    MAX_WEBSITES = int(os.getenv("MAX_WEBSITES_TO_PROCESS", 500))

    @classmethod
    def setup_logging(cls):
        """Configure logging with rich formatting"""
        logging.basicConfig(
            level=getattr(logging, cls.LOG_LEVEL),
            format="%(message)s",
            handlers=[RichHandler()],
        )
        return logging.getLogger(__name__)

    @classmethod
    def validate_config(cls):
        """Validate essential configuration parameters"""
        logger = cls.setup_logging()

        if not cls.BUILTWITH_API_KEY:
            logger.error("❌ BuiltWith API key is missing")
            raise ValueError("BuiltWith API key is required")

        if not cls.HUNTERIO_API_KEY:
            logger.error("❌ Hunter.io API key is missing")
            raise ValueError("Hunter.io API key is required")

        logger.info("✅ Configuration validated successfully")
