from little_syntax.ast_nodes import SayStatement, StringLiteral
from little_syntax.lexer import Token

# the parser turns tokens into AST nodes
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
        if self.match("SAY"):
            return self.say_statement()

        token = self.peek()
        raise LittleSyntaxParserError(
            f"I expected a command like 'say', but found '{token.value}'."
        )

    def say_statement(self):
        value = self.expression()
        return SayStatement(value)

    def expression(self):
        if self.match("STRING"):
            return StringLiteral(self.previous().value)

        token = self.peek()
        raise LittleSyntaxParserError(
            f"I expected a message in quotes, but found '{token.value}'."
        )

    def match(self, token_type: str) -> bool:
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
