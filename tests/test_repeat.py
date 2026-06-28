from little_syntax.runner import run_source


def test_repeat_runs_body_multiple_times():
    result = run_source(
        '''
        repeat 3 {
          say "Glow!"
        }
        '''
    )

    assert result["output"] == ["Glow!", "Glow!", "Glow!"]
    assert result["errors"] == []


def test_repeat_count_can_use_variable():
    result = run_source(
        '''
        let lanterns = 2

        repeat lanterns {
          say "Light!"
        }
        '''
    )

    assert result["output"] == ["Light!", "Light!"]
    assert result["errors"] == []


def test_repeat_count_can_use_math_expression():
    result = run_source(
        '''
        let lanterns = 2

        repeat lanterns + 1 {
          say "Glow!"
        }
        '''
    )

    assert result["output"] == ["Glow!", "Glow!", "Glow!"]
    assert result["errors"] == []


def test_repeat_zero_times_runs_nothing():
    result = run_source(
        '''
        repeat 0 {
          say "This should not appear."
        }
        '''
    )

    assert result["output"] == []
    assert result["errors"] == []


def test_repeat_count_must_be_number():
    result = run_source(
        '''
        repeat "many" {
          say "Glow!"
        }
        '''
    )

    assert result["output"] == []
    assert "repeat count must be a number" in result["errors"][0].lower()


def test_repeat_count_must_be_whole_number():
    result = run_source(
        '''
        repeat 2.5 {
          say "Glow!"
        }
        '''
    )

    assert result["output"] == []
    assert "repeat count must be a whole number" in result["errors"][0].lower()
