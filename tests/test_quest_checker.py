from little_syntax.quest_checker import Quest, check_quest


def test_quest_passes_when_expected_output_matches():
    quest = Quest(
        title="First Spell",
        goal='Print "Hello, traveler!"',
        expected_output=["Hello, traveler!"],
    )

    result = check_quest('say "Hello, traveler!"', quest)

    assert result.passed is True
    assert result.feedback == ["Quest complete!"]
    assert result.output == ["Hello, traveler!"]
    assert result.errors == []


def test_quest_fails_when_expected_output_does_not_match():
    quest = Quest(
        title="First Spell",
        goal='Print "Hello, traveler!"',
        expected_output=["Hello, traveler!"],
    )

    result = check_quest('say "Goodbye!"', quest)

    assert result.passed is False
    assert result.output == ["Goodbye!"]
    assert "Expected output" in result.feedback[0]


def test_quest_can_require_variable():
    quest = Quest(
        title="Name Rune",
        goal="Create a variable named name and store Milo inside it.",
        required_variables={"name": "Milo"},
    )

    result = check_quest(
        '''
        let name = "Milo"
        say name
        ''',
        quest,
    )

    assert result.passed is True
    assert result.feedback == ["Quest complete!"]


def test_quest_fails_when_required_variable_is_missing():
    quest = Quest(
        title="Name Rune",
        goal="Create a variable named name.",
        required_variables={"name": "Milo"},
    )

    result = check_quest('say "Milo"', quest)

    assert result.passed is False
    assert "Create a variable named 'name'" in result.feedback[0]


def test_quest_returns_program_errors_as_feedback():
    quest = Quest(
        title="Name Rune",
        goal="Say the value of name.",
        expected_output=["Milo"],
    )

    result = check_quest("say name", quest)

    assert result.passed is False
    assert result.output == []
    assert len(result.errors) == 1
    assert "I don't know what 'name' means yet" in result.feedback[1]
