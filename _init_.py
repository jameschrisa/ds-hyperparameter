"""
Deepseek R1 Hyperparameter Tuner
A modular CLI tool for managing Deepseek R1 configurations
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

# Make key components available at package level
from .config.manager import ConfigManager
from .config.defaults import DEFAULT_CONFIG
from .utils.logger import setup_logger, get_logger

__all__ = [
    'ConfigManager',
    'DEFAULT_CONFIG',
    'setup_logger',
    'get_logger',
]
