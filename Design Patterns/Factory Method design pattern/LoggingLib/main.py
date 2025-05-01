import os
from logging_lib.factory import get_logger_from_env

def main():
    logger = get_logger_from_env()
    logger.log("DEBUG", "Starting application")
    logger.log("INFO", "Application initialized")
    logger.log("WARNING", "Cache miss, falling back to database")
    logger.log("ERROR", "Failed to process user request")
    logger.log("CRITICAL", "Out of memory, shutting down")

if __name__ == "__main__":
    main()
