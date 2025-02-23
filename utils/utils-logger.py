from pathlib import Path
import logging
from datetime import datetime

def setup_logger():
    """
    Sets up logging configuration with daily rotation
    Returns a configured logger instance
    """
    # Create logs directory if it doesn't exist
    log_dir = Path("data/logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Create a new log file for each day
    log_file = log_dir / f"deepseek_tuner_{datetime.now().strftime('%Y%m%d')}.log"
    
    # Configure logging format and handlers
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()  # Also print to console
        ]
    )
    
    logger = logging.getLogger("deepseek_tuner")
    logger.info("Logger initialized - starting new session")
    
    return logger
