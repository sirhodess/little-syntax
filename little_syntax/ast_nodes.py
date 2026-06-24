from dataclasses import dataclass


class Expr:
    """Base class for expressions."""
    pass


class Stmt:
    """Base class for statements."""
    pass


@dataclass
class StringLiteral(Expr):
    value: str


@dataclass
class SayStatement(Stmt):
    value: Expr
