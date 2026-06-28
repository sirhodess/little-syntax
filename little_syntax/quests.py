from little_syntax.quest_checker import Quest


FIRST_SPELL = Quest(
    title="First Spell",
    goal='Print "Hello, traveler!"',
    expected_output=["Hello, traveler!"],
)


NAME_RUNE = Quest(
    title="Name Rune",
    goal='Create a variable named name and store "Milo" inside it.',
    required_variables={"name": "Milo"},
)


LIGHT_THE_LANTERNS = Quest(
    title="Light the Lanterns",
    goal='Use repeat to print "Glow!" three times.',
    expected_output=["Glow!", "Glow!", "Glow!"],
)


QUESTS = {
    "first-spell": FIRST_SPELL,
    "name-rune": NAME_RUNE,
    "light-the-lanterns": LIGHT_THE_LANTERNS,
}


def get_quest(quest_id: str) -> Quest:
    if quest_id not in QUESTS:
        available = ", ".join(sorted(QUESTS.keys()))
        raise ValueError(
            f"I don't know a quest named '{quest_id}'. Available quests: {available}"
        )

    return QUESTS[quest_id]
