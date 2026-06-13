"""
Logger.py creates a centralized logging system that records application events, warnings, and errors into timestamped log files, making debugging, monitoring, and production maintenance easier than using print statements.

"""


import logging
import os
from datetime import datetime

# Generate a unique log file name for each execution
# Example: 06_13_26_18_45_30.log
LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

# Create logs directory inside the current project folder
# Example: D:/ML_Project/logs
logs_dir = os.path.join(os.getcwd(), "logs")

# Create logs directory if it does not already exist
os.makedirs(logs_dir, exist_ok=True)

# Full path of the log file
# Example: D:/ML_Project/logs/06_13_26_18_45_30.log
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure project-wide logging
logging.basicConfig(
    
    # Destination file for log messages
    filename=LOG_FILE_PATH,

    # Log format:
    # [Timestamp] LineNo LoggerName - Level - Message
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",

    # Record INFO and higher severity logs
    level=logging.INFO,
)

# Example:
# logging.info("Data ingestion started")
# logging.warning("Missing values detected")
# logging.error("Database connection failed")