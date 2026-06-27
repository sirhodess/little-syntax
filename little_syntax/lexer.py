from dataclasses import dataclass


# The lexer turns raw text into tokens.
# Example:
# say "Hello"
#
# becomes:
# SAY
# STRING("Hello")
# EOF


@dataclass
class Token:
    type: str
    value: str


class LittleSyntaxLexerError(Exception):
    pass


KEYWORDS = {
    "say": "SAY",
    "let": "LET",
}


def tokenize(source: str) -> list[Token]:
    tokens: list[Token] = []
    i = 0

    while i < len(source):
        char = source[i]

        if char.isspace():
            i += 1
            continue

        if char == "=":
            tokens.append(Token("EQUAL", "="))
            i += 1
            continue

        if char == '"':
            i += 1
            start = i

            while i < len(source) and source[i] != '"':
                i += 1

            if i >= len(source):
                raise LittleSyntaxLexerError(
                    "You started a message with a quote, but forgot the closing quote."
                )

            value = source[start:i]
            tokens.append(Token("STRING", value))
            i += 1
            continue

        if char.isalpha() or char == "_":
            start = i

            while i < len(source) and (source[i].isalnum() or source[i] == "_"):
                i += 1

            text = source[start:i]
            token_type = KEYWORDS.get(text, "IDENTIFIER")
            tokens.append(Token(token_type, text))
            continue

        raise LittleSyntaxLexerError(f"I don't understand this character yet: {char}")

    tokens.append(Token("EOF", ""))
    return tokens
