from little_syntax.ast_nodes import (
    BinaryExpression,
    LetStatement,
    NumberLiteral,
    SayStatement,
    StringLiteral,
    VariableExpression,
)


Value = str | int | float


class LittleSyntaxRuntimeError(Exception):
    pass


class Interpreter:
    def __init__(self):
        self.output: list[str] = []
        self.environment: dict[str, Value] = {}

    def run(self, statements):
        for statement in statements:
            self.execute(statement)

        return {
            "output": self.output,
            "errors": [],
            "variables": self.environment.copy(),
        }

    def execute(self, statement):
        if isinstance(statement, LetStatement):
            value = self.evaluate(statement.value)
            self.environment[statement.name] = value
            return

        if isinstance(statement, SayStatement):
            value = self.evaluate(statement.value)
            self.output.append(self.stringify(value))
            return

        raise LittleSyntaxRuntimeError("I don't know how to run that statement yet.")

    def evaluate(self, expression) -> Value:
        if isinstance(expression, StringLiteral):
            return expression.value

        if isinstance(expression, NumberLiteral):
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

            raise LittleSyntaxRuntimeError(
                f"I don't know how to use the operator '{expression.operator}' yet."
            )

        raise LittleSyntaxRuntimeError("I don't know how to understand that expression yet.")

    def require_numbers(
        self,
        left: Value,
        right: Value,
        operator: str,
    ) -> tuple[int | float, int | float]:
        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
            raise LittleSyntaxRuntimeError(
                f"The '{operator}' operator only works with numbers right now."
            )

        return left, right

    def stringify(self, value: Value) -> str:
        if isinstance(value, float) and value.is_integer():
            return str(int(value))

        return str(value)