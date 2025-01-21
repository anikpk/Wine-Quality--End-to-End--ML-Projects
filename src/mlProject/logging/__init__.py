import os
import sys
import logging

# Set up the logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the log directory and file path
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_log.log")

# Create the logs directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the minimum logging level
    format=logging_str,  # Set the log format
    handlers=[
        logging.FileHandler(log_filepath),  # Log to a file
        logging.StreamHandler(sys.stdout)   # Log to stdout (console)
    ]
)

# Create and configure the logger
logger = logging.getLogger("mlProjectLogger")