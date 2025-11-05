"""
Python file to set up a logging function.
"""

import logging


def my_logger():
    """
    Function that builds a logger and writes logs to a file and console.
    Prevents duplicate handlers.
    """
    logger = logging.getLogger(__name__)
    
    # Only configure the logger if it hasn't been configured before
    if not logger.handlers:

        logger.setLevel(logging.INFO)

        # Create the log file handler (INFO level)

        log_file_handler = logging.FileHandler('currency_logger.log')
        log_file_handler.setLevel(logging.INFO)
        log_file_formatter = logging.Formatter(
            "line %(lineno)d. - %(levelname)s - %(message)s - %(asctime)s")
        log_file_handler.setFormatter(log_file_formatter)
        
        # Create the log stream handler (WARNING level)
        log_stream_handler = logging.StreamHandler()
        log_stream_handler.setLevel(logging.WARNING)
        log_stream_formatter = logging.Formatter(
            "line %(lineno)d. - %(levelname)s - %(message)s ")
        log_stream_handler.setFormatter(log_stream_formatter)

        # Add both handlers to the same logger
        logger.addHandler(log_file_handler)
        logger.addHandler(log_stream_handler)

    return logger

if __name__ == "__main__":
    my_logger()
    