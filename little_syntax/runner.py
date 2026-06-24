import sys

from little_syntax.interpreter import Interpreter
from little_syntax.lexer import tokenize
from little_syntax.parser import Parser

# becomes the one clean entry point once FastAPI is set up
# but for now, the terminal can run .ls files

def run_source(source: str):
    try:
        tokens = tokenize(source)
        statements = Parser(tokens).parse()
        return Interpreter().run(statements)

    except Exception as error:
        return {
            "output": [],
            "errors": [str(error)],
            "variables": {},
        }


def run_file(path: str):
    with open(path, "r", encoding="utf-8") as file:
        source = file.read()

    return run_source(source)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 -m little_syntax.runner path/to/file.ls")
        raise SystemExit(1)

    result = run_file(sys.argv[1])

    for line in result["output"]:
        print(line)

    for error in result["errors"]:
        print(f"Error: {error}")
