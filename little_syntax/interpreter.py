from typing import TypeGuard

from little_syntax.ast_nodes import (
    BinaryExpression,
    BooleanLiteral,
    Expr,
    IfStatement,
    LetStatement,
    NumberLiteral,
    RepeatStatement,
    SayStatement,
    Stmt,
    StringLiteral,
    VariableExpression,
)


Value = str | int | float | bool
NumberValue = int | float


def is_number_value(value: Value) -> TypeGuard[NumberValue]:
    return type(value) in (int, float)


class LittleSyntaxRuntimeError(Exception):
    pass


class Interpreter:
    def __init__(self):
        self.output: list[str] = []
        self.environment: dict[str, Value] = {}

    def run(self, statements: list[Stmt]):
        for statement in statements:
            self.execute(statement)

        return {
            "output": self.output,
            "errors": [],
            "variables": self.environment.copy(),
        }

    def execute(self, statement: Stmt) -> None:
        if isinstance(statement, LetStatement):
            value = self.evaluate(statement.value)
            self.environment[statement.name] = value
            return

        if isinstance(statement, SayStatement):
            value = self.evaluate(statement.value)
            self.output.append(self.stringify(value))
            return

        if isinstance(statement, IfStatement):
            condition = self.evaluate(statement.condition)

            if not isinstance(condition, bool):
                raise LittleSyntaxRuntimeError(
                    "An if condition must be true or false. "
                    "Try using a comparison like: if coins >= 5"
                )

            branch = statement.then_branch if condition else statement.else_branch

            if branch is not None:
                for nested_statement in branch:
                    self.execute(nested_statement)

            return

        if isinstance(statement, RepeatStatement):
            count_value = self.evaluate(statement.count)
            repeat_count = self.require_repeat_count(count_value)

            for _ in range(repeat_count):
                for nested_statement in statement.body:
                    self.execute(nested_statement)

            return

        raise LittleSyntaxRuntimeError("I don't know how to run that statement yet.")

    def evaluate(self, expression: Expr) -> Value:
        if isinstance(expression, StringLiteral):
            return expression.value

        if isinstance(expression, NumberLiteral):
            return expression.value

        if isinstance(expression, BooleanLiteral):
            return expression.value

        if isinstance(expression, VariableExpression):
            if expression.name not in self.environment:
                raise LittleSyntaxRuntimeError(
                    f"I don't know what '{expression.name}' means yet. "
                    f"Try creating it first with: let {expression.name} = ..."
                )

            return self.environment[expression.name]

        if isinstance(expression, BinaryExpression):
            left = self.evaluate(expression.left)
            right = self.evaluate(expression.right)

            if expression.operator in ("+", "-", "*", "/"):
                left_number, right_number = self.require_numbers(
                    left,
                    right,
                    expression.operator,
                )

                if expression.operator == "+":
                    return left_number + right_number

                if expression.operator == "-":
                    return left_number - right_number

                if expression.operator == "*":
                    return left_number * right_number

                if expression.operator == "/":
                    if right_number == 0:
                        raise LittleSyntaxRuntimeError(
                            "You tried to divide by zero, but division by zero is not allowed."
                        )

                    return left_number / right_number

            if expression.operator in (">", ">=", "<", "<="):
                left_number, right_number = self.require_numbers(
                    left,
                    right,
                    expression.operator,
                )

                if expression.operator == ">":
                    return left_number > right_number

                if expression.operator == ">=":
                    return left_number >= right_number

                if expression.operator == "<":
                    return left_number < right_number

                if expression.operator == "<=":
                    return left_number <= right_number

            if expression.operator == "==":
                return left == right

            if expression.operator == "!=":
                return left != right

            raise LittleSyntaxRuntimeError(
                f"I don't know how to use the operator '{expression.operator}' yet."
            )

        raise LittleSyntaxRuntimeError("I don't know how to understand that expression yet.")

    def require_numbers(
        self,
        left: Value,
        right: Value,
        operator: str,
    ) -> tuple[NumberValue, NumberValue]:
        if not is_number_value(left):
            raise LittleSyntaxRuntimeError(
                f"The '{operator}' operator only works with numbers right now."
            )

        if not is_number_value(right):
            raise LittleSyntaxRuntimeError(
                f"The '{operator}' operator only works with numbers right now."
            )

        return left, right

    def require_repeat_count(self, count: Value) -> int:
        if not is_number_value(count):
            raise LittleSyntaxRuntimeError(
                "The repeat count must be a number. Example: repeat 3 { say \"Glow!\" }"
            )

        if isinstance(count, float) and not count.is_integer():
            raise LittleSyntaxRuntimeError(
                "The repeat count must be a whole number like 1, 2, or 3."
            )

        if count < 0:
            raise LittleSyntaxRuntimeError(
                "The repeat count cannot be negative."
            )

        return int(count)

    def stringify(self, value: Value) -> str:
        if isinstance(value, bool):
            return "true" if value else "false"

        if isinstance(value, float) and value.is_integer():
            return str(int(value))

        return str(value)
