from little_syntax.ast_nodes import (
    BinaryExpression,
    LetStatement,
    NumberLiteral,
    SayStatement,
    StringLiteral,
    VariableExpression,
)
from little_syntax.lexer import Token


class LittleSyntaxParserError(Exception):
    pass


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        statements = []

        while not self.is_at_end():
            statements.append(self.statement())

        return statements

    def statement(self):
        if self.match("LET"):
            return self.let_statement()

        if self.match("SAY"):
            return self.say_statement()

        token = self.peek()
        raise LittleSyntaxParserError(
            f"I expected a command like 'let' or 'say', but found '{token.value}'."
        )

    def let_statement(self):
        name = self.consume(
            "IDENTIFIER",
            "I expected a variable name after 'let'. Example: let name = \"Milo\"",
        )

        self.consume(
            "EQUAL",
            f"I expected '=' after the variable name '{name.value}'.",
        )

        value = self.expression()
        return LetStatement(name.value, value)

    def say_statement(self):
        value = self.expression()
        return SayStatement(value)

    def expression(self):
        return self.addition()

    def addition(self):
        expression = self.multiplication()

        while self.match("PLUS", "MINUS"):
            operator = self.previous().value
            right = self.multiplication()
            expression = BinaryExpression(expression, operator, right)

        return expression

    def multiplication(self):
        expression = self.primary()

        while self.match("STAR", "SLASH"):
            operator = self.previous().value
            right = self.primary()
            expression = BinaryExpression(expression, operator, right)

        return expression

    def primary(self):
        if self.match("STRING"):
            return StringLiteral(self.previous().value)

        if self.match("NUMBER"):
            value = self.previous().value

            if "." in value:
                return NumberLiteral(float(value))

            return NumberLiteral(int(value))

        if self.match("IDENTIFIER"):
            return VariableExpression(self.previous().value)

        if self.match("LEFT_PAREN"):
            expression = self.expression()
            self.consume("RIGHT_PAREN", "I expected ')' after this expression.")
            return expression

        token = self.peek()
        raise LittleSyntaxParserError(
            f"I expected a value like a number, message, or variable name, but found '{token.value}'."
        )

    def consume(self, token_type: str, message: str) -> Token:
        if self.check(token_type):
            return self.advance()

        raise LittleSyntaxParserError(message)

    def match(self, *token_types: str) -> bool:
        for token_type in token_types:
            if self.check(token_type):
                self.advance()
                return True

        return False

    def check(self, token_type: str) -> bool:
        if self.is_at_end():
            return False

        return self.peek().type == token_type

    def advance(self) -> Token:
        if not self.is_at_end():
            self.current += 1

        return self.previous()

    def is_at_end(self) -> bool:
        return self.peek().type == "EOF"

    def peek(self) -> Token:
        return self.tokens[self.current]

    def previous(self) -> Token:
        return self.tokens[self.current - 1]
