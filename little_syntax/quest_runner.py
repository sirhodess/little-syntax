import sys

from little_syntax.quest_checker import check_quest
from little_syntax.quests import get_quest


def run_quest_file(quest_id: str, path: str) -> int:
    quest = get_quest(quest_id)

    with open(path, "r", encoding="utf-8") as file:
        source = file.read()

    result = check_quest(source, quest)

    print(f"Quest: {quest.title}")
    print(f"Goal: {quest.goal}")
    print()

    if result.output:
        print("Output:")
        for line in result.output:
            print(line)
        print()

    print("Feedback:")
    for message in result.feedback:
        print(message)

    return 0 if result.passed else 1


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 -m little_syntax.quest_runner quest-id path/to/file.ls")
        raise SystemExit(1)

    quest_id = sys.argv[1]
    path = sys.argv[2]

    try:
        exit_code = run_quest_file(quest_id, path)
        raise SystemExit(exit_code)
    except Exception as error:
        print(f"Error: {error}")
        raise SystemExit(1)
