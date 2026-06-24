from dataclasses import dataclass

# the lexer turns raw text into tokens.
# say "Hello"
# SAY
# STRING("Hello")
# EOF
@dataclass
class Token:
    type: str
    value: str


class LittleSyntaxLexerError(Exception):
    pass

def tokenize(source: str) -> list[Token]:
    tokens: list[Token] = []
    i = 0

    while i < len(source):
        char = source[i]

        if char.isspace():
            i += 1
            continue

        if source.startswith("say", i):
            tokens.append(Token("SAY", "say"))
            i += 3
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

        raise LittleSyntaxLexerError(f"I don't understand this character yet: {char}")

    tokens.append(Token("EOF", ""))
    return tokens
