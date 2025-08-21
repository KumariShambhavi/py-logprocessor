# py-logprocessor

A lightweight and modular Python package for **log processing and timing utilities**.  
It helps developers measure execution times, process logs efficiently, and structure log records in a clean, testable way.

---

## ✨ Features

- 📜 **Structured log records** with `LogRecord` and `LogFactory`
- ⏱ **Execution timing** using `Timer` (context manager + decorator)
- ⚡ **Lightweight log processor** with error/success reporting
- ✅ **Fully tested** with `pytest`
- 🛠 **Easy to integrate** into any Python project

---

## 📂 Project Structure

py-logprocessor/
│
├── logprocessor/ # Core package
│ ├── init.py
│ ├── main.py # Entry point (run with python -m logprocessor)
│ ├── models.py # LogRecord, LogFactory
│ ├── processor.py # Process logs with timing
│ └── timing.py # Timer utilities
│
├── tests/ # Unit tests (pytest)
│ ├── test_models.py
│ └── test_timing.py
│
├── main.py # Example usage script
├── report.md # Project report / documentation
├── LICENSE # MIT License




---

## 🚀 Installation

Clone the repository:


git clone https://github.com/KumariShambhavi/py-logprocessor.git
cd py-logprocessor
(Optional) Create a virtual environment:

e
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
Install dependencies (only pytest for testing):


pip install -r requirements.txt
▶️ Usage
Run the processor directly:


python -m logprocessor
Or use the example script:


python main.py
Sample output:


[ERROR] failed (at 1755754411.98)
[INFO] started (at 1755754411.98)
[INFO] process_logs took 0.0000 seconds (at 1755754411.98)
🧪 Running Tests
All tests are written with pytest.


Expected output:


tests/test_models.py::test_logrecord_str PASSED
tests/test_models.py::test_logfactory_creates_record PASSED
tests/test_timing.py::test_timer_context_manager PASSED
tests/test_timing.py::test_time_function_decorator PASSED


📜 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this software with proper attribution.
See the LICENSE file for full details.

💡 Applications
Performance benchmarking for Python functions

Building structured logging into larger projects

Teaching core concepts of OOP, decorators, and context managers

Lightweight alternative for simple log/timing tasks

👩‍💻 Author
Kumari Shambhavi
GitHub Profile
