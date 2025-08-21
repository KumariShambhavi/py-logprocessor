from .models import LogFactory, LogRecord
from .timing import time_function
from typing import List


class LogProcessor:
    """Handles log processing with timing support."""

    @time_function
    def process_logs(self) -> List[LogRecord]:
        logs = [
            LogFactory.create("error", "failed"),
            LogFactory.create("info", "started")
        ]
        for log in logs:
            print(log)
        return logs
