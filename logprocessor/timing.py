import time
from typing import Callable, Any
from .models import LogFactory, LogRecord


class Timer:
    """Context manager to measure execution time."""
    def __init__(self, task_name: str = "Task"):
        self.task_name = task_name
        self.start: float = 0.0
        self.duration: float = 0.0
        self.log: LogRecord | None = None

    def __enter__(self) -> "Timer":
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.duration = time.time() - self.start
        self.log = LogFactory.create(
            level="info",
            message=f"{self.task_name} took {self.duration:.4f} seconds"
        )
        print(self.log)


def time_function(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that times function execution using Timer."""
    def wrapper(*args, **kwargs):
        with Timer(func.__name__):
            return func(*args, **kwargs)
    return wrapper
