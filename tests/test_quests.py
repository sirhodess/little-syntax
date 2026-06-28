import pytest

from little_syntax.quests import get_quest


def test_get_quest_returns_known_quest():
    quest = get_quest("first-spell")

    assert quest.title == "First Spell"
    assert quest.expected_output == ["Hello, traveler!"]


def test_get_quest_rejects_unknown_quest():
    with pytest.raises(ValueError) as error:
        get_quest("missing-quest")

    assert "I don't know a quest named 'missing-quest'" in str(error.value)
