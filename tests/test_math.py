from little_syntax.runner import run_source


def test_say_number_math():
    result = run_source("say 3 + 2")

    assert result["output"] == ["5"]
    assert result["errors"] == []


def test_math_uses_operator_precedence():
    result = run_source("say 3 + 2 * 4")

    assert result["output"] == ["11"]
    assert result["errors"] == []


def test_parentheses_group_math():
    result = run_source("say (3 + 2) * 4")

    assert result["output"] == ["20"]
    assert result["errors"] == []


def test_variable_can_store_number():
    result = run_source(
        '''
        let coins = 3
        say coins + 2
        '''
    )

    assert result["output"] == ["5"]
    assert result["errors"] == []
    assert result["variables"] == {"coins": 3}


def test_dividing_by_zero_returns_friendly_error():
    result = run_source("say 10 / 0")

    assert result["output"] == []
    assert "divide by zero" in result["errors"][0]
