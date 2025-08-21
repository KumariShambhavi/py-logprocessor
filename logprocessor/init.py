# logprocessor/__init__.py
"""logprocessor package — small utilities for creating and timing LogRecords.

Public exports:
- LogRecord, LogFactory
- Timer, time_function
- LogProcessor

Keep this file lightweight to avoid side-effects on import.
"""
from .models import LogRecord, LogFactory
from .timing import Timer, time_function
from .processor import LogProcessor

__all__ = [
    "LogRecord",
    "LogFactory",
    "Timer",
    "time_function",
    "LogProcessor",
]

__version__ = "0.1.0"
__author__ = "Kumari Shambhavi"
