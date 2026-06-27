from little_syntax.runner import run_source


def test_let_stores_variable_and_say_reads_it():
    result = run_source(
        '''
        let name = "Milo"
        say name
        '''
    )

    assert result["output"] == ["Milo"]
    assert result["errors"] == []
    assert result["variables"] == {"name": "Milo"}


def test_say_unknown_variable_returns_friendly_error():
    result = run_source("say name")

    assert result["output"] == []
    assert len(result["errors"]) == 1
    assert "I don't know what 'name' means yet" in result["errors"][0]
