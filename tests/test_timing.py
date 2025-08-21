from logprocessor.timing import Timer, time_function


def test_timer_context_manager():
    with Timer("sample") as t:
        pass
    assert t.duration >= 0
    assert "took" in t.log.message


def test_time_function_decorator():
    @time_function
    def dummy():
        return 42
    result = dummy()
    assert result == 42
