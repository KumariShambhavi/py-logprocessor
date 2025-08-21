

### `logprocessor/models.py`

from dataclasses import dataclass
from time import time


@dataclass
class LogRecord:
    """Represents a structured log entry."""
    timestamp: float
    level: str
    message: str

    def __str__(self) -> str:
        return f"[{self.level.upper()}] {self.message} (at {self.timestamp:.2f})"


class LogFactory:
    """Factory for creating LogRecord instances."""
    @staticmethod
    def create(level: str, message: str) -> LogRecord:
        return LogRecord(timestamp=time(), level=level, message=message)
