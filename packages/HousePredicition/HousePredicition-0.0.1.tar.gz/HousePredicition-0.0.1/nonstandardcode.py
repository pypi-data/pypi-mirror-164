import argparse
from pathlib import Path
import logging


logger = logging.getLogger(__name__)


def dummy_function():
    """Dummy Function to test logging inside a function"""
    logger.info(f"Logging Test - Function Call Object Done")
