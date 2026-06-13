""" 

exception.py file used in end-to-end ML projects. Its purpose is to create custom error messages with file name and line number information, making debugging much easier.

"""

import sys
from src.logger import logging


# Extract detailed exception information
# (file name, line number, original error)
def error_message_detail(error, error_detail: sys):

    # Get exception traceback object
    _, _, exc_tb = error_detail.exc_info()

    # File where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create detailed error message
    error_message = (
        f"Error occurred in python script [{file_name}] "
        f"at line number [{exc_tb.tb_lineno}] "
        f"error message [{str(error)}]"
    )

    return error_message


# Custom exception class used across the project
class CustomException(Exception):

    def __init__(self, error_message, error_detail: sys):

        # Initialize parent Exception class
        super().__init__(error_message)

        # Store detailed exception information
        self.error_message = error_message_detail(
            error_message,
            error_detail=error_detail
        )

    # Controls what gets printed when exception object is displayed
    def __str__(self):
        return self.error_message