from little_syntax.ast_nodes import SayStatement, StringLiteral

# the interpreter actually runs the AST

class LittleSyntaxRuntimeError(Exception):
    pass


class Interpreter:
    def __init__(self):
        self.output: list[str] = []

    def run(self, statements):
        for statement in statements:
            self.execute(statement)

        return {
            "output": self.output,
            "errors": [],
            "variables": {},
        }

    def execute(self, statement):
        if isinstance(statement, SayStatement):
            value = self.evaluate(statement.value)
            self.output.append(value)
            return

        raise LittleSyntaxRuntimeError("I don't know how to run that statement yet.")

    def evaluate(self, expression):
        if isinstance(expression, StringLiteral):
            return expression.value

        raise LittleSyntaxRuntimeError("I don't know how to understand that expression yet.")
