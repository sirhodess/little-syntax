from little_syntax.runner import run_source


def test_if_runs_then_branch_when_condition_is_true():
    result = run_source(
        '''
        let coins = 5

        if coins >= 5 {
          say "The gate opens!"
        } else {
          say "You need more coins."
        }
        '''
    )

    assert result["output"] == ["The gate opens!"]
    assert result["errors"] == []


def test_if_runs_else_branch_when_condition_is_false():
    result = run_source(
        '''
        let coins = 2

        if coins >= 5 {
          say "The gate opens!"
        } else {
          say "You need more coins."
        }
        '''
    )

    assert result["output"] == ["You need more coins."]
    assert result["errors"] == []


def test_if_without_else_does_nothing_when_false():
    result = run_source(
        '''
        let coins = 2

        if coins >= 5 {
          say "The gate opens!"
        }
        '''
    )

    assert result["output"] == []
    assert result["errors"] == []


def test_boolean_values_can_be_printed():
    result = run_source(
        '''
        say true
        say false
        '''
    )

    assert result["output"] == ["true", "false"]
    assert result["errors"] == []


def test_equality_operators_work():
    result = run_source(
        '''
        say 5 == 5
        say 5 != 3
        say 5 == 3
        '''
    )

    assert result["output"] == ["true", "true", "false"]
    assert result["errors"] == []


def test_if_condition_must_be_boolean():
    result = run_source(
        '''
        let coins = 5

        if coins {
          say "This should not run."
        }
        '''
    )

    assert result["output"] == []
    assert "if condition must be true or false" in result["errors"][0].lower()