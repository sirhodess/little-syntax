from little_syntax.runner import run_source


def test_say_outputs_string():
    result = run_source('say "Hello, traveler!"')

    assert result["output"] == ["Hello, traveler!"]
    assert result["errors"] == []
    assert result["variables"] == {}
