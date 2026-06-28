# Little Syntax Milestones

Little Syntax is being bult in small, testable milestones. Each milestone adds one new piece of the language or learning experience.

## Milestone 0: Project Setup

**Goal:** Create the base project structure.

- [x] Create Python package folder
- [x] Add examples folder
- [x] Add tests folder
- [x] Add first `.ls` example file

## Status: Complete

## Milestone 1: Say Command

**Goal:** Run the first Little Syntax program.

Example:

```ls
say "Hello, traveler!"
```

- [x] Create AST nodes
- [x] Create lexer
- [x] Create parser
- [x] Create interpreter
- [x] Add `run_source()` helper
- [x] Add first test

Status: Complete

---

## Milestone 2: Variables

**Goal:** Let learners store and reuse values.

Example:

```ls
let name = "Milo"
say name

Expected output: Milo
```

Status: Complete

---

## Milestone 3: Numbers and Math

**Goal:** Let learners use numbers and basic arithmetic.

Example:

```ls
let coins = 3
say coins + 2

Expected output: 5
```

Status: Complete

---

## Milestone 4: Conditionals

**Goal:** Let learners make choices with `if` and `else`.

Example:

```ls
let coins = 5

if coins >= 5 {
  say "The gate opens!"
} else {
  say "You need more coins."
}

Expected output: The gate opens!
```

Tasks:

- [x] Add `if` keyword
- [x] Add `else` keyword
- [x] Add boolean values with `true` and `false`
- [x] Add comparison operators: `>`, `>=`, `<`, `<=`
- [x] Add equality operators: `==`, `!=`
- [x] Add block parsing with `{ }`
- [x] Add `if` statement execution
- [x] Add optional `else` branch
- [x] Add friendly error for non-boolean conditions
- [x] Add conditional example file
- [x] Add conditional tests

---

## Milestone 5: Loops with Repeat

**Goal:** Let learners repeat actions with `repeat`.

Example:

```ls
repeat 3 {
  say "Glow!"
}

Expected Output:

Glow!
Glow!
Glow!
```

Tasks:

- [x] Add `repeat` keyword
- [x] Add `repeat` AST node
- [x] Add `repeat` parsing
- [x] Allow `repeat` counts to use variables
- [x] Allow `repeat` counts to use math expressions
- [x] Execute `repeat` block multiple times
- [x] Add friendly error for non-number `repeat` counts
- [x] Add friendly error for decimal `repeat` counts
- [x] Add `repeat` example file
- [x] Add `repeat` tests

Status: Complete
