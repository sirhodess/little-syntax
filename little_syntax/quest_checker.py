from dataclasses import dataclass, field
from typing import Any

from little_syntax.runner import run_source


@dataclass
class Quest:
    title: str
    goal: str
    expected_output: list[str] = field(default_factory=list)
    required_variables: dict[str, Any] = field(default_factory=dict)


@dataclass
class QuestResult:
    passed: bool
    feedback: list[str]
    output: list[str]
    errors: list[str]


def check_quest(source: str, quest: Quest) -> QuestResult:
    run_result = run_source(source)

    output = run_result["output"]
    errors = run_result["errors"]
    variables = run_result["variables"]

    feedback: list[str] = []

    if errors:
        return QuestResult(
            passed=False,
            feedback=[
                "Your code ran into an error. Fix the error and try again.",
                *errors,
            ],
            output=output,
            errors=errors,
        )

    if quest.expected_output and output != quest.expected_output:
        feedback.append(
            f"Expected output {quest.expected_output}, but got {output}."
        )

    for variable_name, expected_value in quest.required_variables.items():
        if variable_name not in variables:
            feedback.append(
                f"Create a variable named '{variable_name}' to complete this quest."
            )
            continue

        actual_value = variables[variable_name]
        if actual_value != expected_value:
            feedback.append(
                f"Expected '{variable_name}' to be {expected_value}, but got {actual_value}."
            )

    passed = len(feedback) == 0

    if passed:
        feedback.append("Quest complete!")

    return QuestResult(
        passed=passed,
        feedback=feedback,
        output=output,
        errors=errors,
    )
