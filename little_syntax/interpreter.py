from little_syntax.ast_nodes import (
    LetStatement,
    SayStatement,
    StringLiteral,
    VariableExpression,
)

# interpreter actually runs the AST nodes

class LittleSyntaxRuntimeError(Exception):
    pass


class Interpreter:
    def __init__(self):
        self.output: list[str] = []
        self.environment: dict[str, object] = {}

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
            self.output.append(str(value))
            return

        raise LittleSyntaxRuntimeError("I don't know how to run that statement yet.")

    def evaluate(self, expression):
        if isinstance(expression, StringLiteral):
            return expression.value

        if isinstance(expression, VariableExpression):
            if expression.name not in self.environment:
                raise LittleSyntaxRuntimeError(
                    f"I don't know what '{expression.name}' means yet. "
                    f"Try creating it first with: let {expression.name} = ..."
                )

            return self.environment[expression.name]

        raise LittleSyntaxRuntimeError("I don't know how to understand that expression yet.")