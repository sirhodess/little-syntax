from dataclasses import dataclass

# meaning 
# say "Hello"
# becomes SayStatement(StringLiteral("Hello"))
class Expr:
    """Base class for expressions."""
    pass


class Stmt:
    """Base class for statements."""
    pass


@dataclass
class StringLiteral(Expr):
    value: str

#look up the value stored under name
@dataclass
class VariableExpression(Expr):
    name: str

@dataclass
class SayStatement(Stmt):
    value: Expr

#store "Milo" in a variable called name.
@dataclass
class LetStatement(Stmt):
    name: str
    value: Expr
