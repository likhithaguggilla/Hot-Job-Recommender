"""
LOGGING UTILITY
Purpose: Provides a standardized, professional logging interface for the application.
Functionality:
    - Replaces standard print() statements with leveled logs (INFO, WARNING, ERROR).
    - Includes timestamps, module names, and severity levels for easier debugging.
    - Prevents duplicate log entries by checking for existing handlers.
    - Streams all output to sys.stdout for compatibility with cloud logging services.
"""

import logging
import sys

def get_logger(name: str):
    """
    Creates and configures a logger instance for a specific module.
    
    Args:
        name (str): The name of the module requesting the logger (typically __name__).
        
    Returns:
        logging.Logger: A configured logger instance.
    """
    # Create a logger associated with the module name
    logger = logging.getLogger(name)
    
    # Set the threshold for what messages to capture. 
    # INFO captures general events, WARNINGs, and ERRORs.
    logger.setLevel(logging.INFO)

    # Define a professional format: 
    # YYYY-MM-DD HH:MM:SS,ms - ModuleName - Level - Message
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Stream to console (sys.stdout)
    # This ensures logs appear in terminal and are captured by Docker/Cloud logs.
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    
    # Crucial Production Check: Only add the handler if one doesn't exist.
    # This prevents the same message from being printed multiple times 
    # when a logger is called repeatedly in the same session.
    if not logger.handlers:
        logger.addHandler(handler)
        
    return logger

# ------ Usage Example ------
#
# from src.utils.logger import get_logger
# logger = get_logger(__name__)
# logger.info("Application started successfully.")