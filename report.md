# Advanced Python Concepts and Practical Exercises

## Objective
The goal of this exercise was to explore advanced Python concepts including dataclasses, dunder methods, context managers, SOLID principles, and the Factory Method pattern.  
These concepts were then applied to refactor a poorly structured script into a clean Python package with unit tests.

---

## 1. Classes vs. Dataclasses
### Learnings
- **Traditional Classes** require boilerplate (`__init__`, `__repr__`, etc.).
- **Dataclasses** (Python 3.7+) auto-generate these dunder methods, reducing boilerplate.
- Use **dataclasses** for data-holding structures; use **classes** when behavior dominates.
- Limitation: Dataclasses don't enforce immutability unless `frozen=True`.

**Snippet tested:**
```python
from dataclasses import dataclass

@dataclass
class LogRecord:
    timestamp: float
    level: str
    message: str
2. Dunder Methods & Context Managers
Learnings
Common dunder methods:

__init__: initialization

__str__: user-friendly string

__repr__: unambiguous string

__enter__/__exit__: context managers

Context managers ensure proper setup/teardown of resources.

Built-in contextlib.contextmanager is a lightweight alternative.

Snippet tested:


from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    yield
    print(f"Duration: {time.time() - start}")
3. SOLID & Clean Code in Python
Learnings
Single Responsibility: One class = one purpose (LogRecord for logs, Timer for timing).

Open/Closed: Processor can accept new log types without modifying core.

Liskov Substitution: Functions should work with base or derived classes interchangeably.

Interface Segregation: Avoid "fat" interfaces; small, focused abstractions.

Dependency Inversion: Depend on abstractions, not concretions.

Applied via:

Separation of models, timing, processor.

Type hints & interfaces where possible.

4. Factory Method Pattern
Learnings
Useful when creating objects dynamically.

Manager decides which class to instantiate based on input.

Example: A LogFactory could generate ErrorLog or InfoLog.

Snippet tested:


class LogFactory:
    @staticmethod
    def create(level: str, message: str):
        from time import time
        return LogRecord(timestamp=time(), level=level, message=message)
Conclusion
Through this task, I learned:

Dataclasses simplify data representation.

Context managers make resource handling safer.

SOLID keeps code maintainable and testable.

Factory methods add flexibility in object creation.

I applied these concepts to refactor the spaghetti script into a modular, testable Python package.



---

## 📦 Package Structure

logprocessor/
│── init.py
│── models.py # LogRecord dataclass
│── timing.py # Context manager for timing
│── processor.py # Log processing logic
tests/
│── test_models.py # Unit tests for LogRecord
│── test_timing.py # Unit tests for timing
report.md


