import time
from logprocessor.models import LogFactory, LogRecord


def test_logrecord_str():
    log = LogRecord(timestamp=123456.0, level="info", message="test")
    assert "INFO" in str(log)
    assert "test" in str(log)


def test_logfactory_creates_record():
    log = LogFactory.create("error", "something failed")
    assert isinstance(log, LogRecord)
    assert log.level == "error"
    assert "failed" in log.message
    assert log.timestamp <= time.time()
