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
class NumberLiteral(Expr):
    value: int | float


@dataclass
class BooleanLiteral(Expr):
    value: bool


@dataclass
class VariableExpression(Expr):
    name: str


@dataclass
class BinaryExpression(Expr):
    left: Expr
    operator: str
    right: Expr


@dataclass
class SayStatement(Stmt):
    value: Expr


@dataclass
class LetStatement(Stmt):
    name: str
    value: Expr


@dataclass
class IfStatement(Stmt):
    condition: Expr
    then_branch: list[Stmt]
    else_branch: list[Stmt] | None = None
