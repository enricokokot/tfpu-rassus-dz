import logging

def configure_logging():
    # Configure logging to display messages of level INFO and above to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Configure logging to write messages of level WARNING and above to the app_log.log file
    file_handler = logging.FileHandler('app_log.log')
    file_handler.setLevel(logging.WARNING)

    # Create a formatter to include timestamps in log messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Set the formatter for both console and file handlers
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Get the root logger and add the configured handlers
    root_logger = logging.getLogger()
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
    # Also a possible way of editing how the LOG file will look like
    '''
    logging.basicConfig(filename=log_file_path
                    , level=logging.INFO 
                    , format='%(asctime)s - %(message)s'
                    , datefmt='%d-%m-%Y %H:%M:%S'
    )
    '''

def demonstrate_logging():
    # Log messages of different levels
    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")

if __name__ == "__main__":
    # Configure logging settings
    configure_logging()

    # Demonstrate logging
    demonstrate_logging()
