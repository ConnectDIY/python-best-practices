import logging
import sys

"""
Copy the module and just import the logger everywhere
"""

FORMATTER = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s")

logger = logging.getLogger('your_app_name')
if not logger.handlers:
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    logger.addHandler(console_handler)
