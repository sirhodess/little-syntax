# Little Syntax

Little Syntax is a beginner-friendly educational programming language and interactive coding quest board.

The project combines a custom interpreter, a FastAPI backend, and a React frontend to create a playful learning environment where users solve tiny fantasy quests with simple code.

Learners write Little Syntax programs to help characters move through a storybook-style board, complete quests, and practice foundational programming concepts like output, variables, loops, conditionals, and expressions.

## Project Vision

Little Syntax is designed to make early programming concepts feel approachable, visual, and playful.

Instead of starting with abstract syntax alone, learners interact with a small fantasy quest world. Code becomes the way they wake the map, light the path, and solve problems for characters.

The long-term goal is to build a gamified learning experience where each quest introduces a programming concept through story, feedback, and visible progression.

## Current Features

- Custom lexer for tokenizing Little Syntax source code
- Recursive descent parser for building an abstract syntax tree
- Interpreter for executing Little Syntax programs
- Support for strings, numbers, booleans, variables, math, conditionals, and repeat loops
- Friendly error messages designed for beginners
- Quest checker prototype for validating learner solutions
- FastAPI backend with a `/run` endpoint
- React + Vite frontend
- Full-page fantasy quest board UI
- Toggleable code drawer for writing and running code
- Multi-step quest progression
- Canvas-based dragon intro animation
- Automated Python test suite

## Little Syntax Examples

### Output

```ls
say "Hello, traveler!"
```

### Variables

```ls
let name = "Milo"
say name
```

### Math

```ls
let coins = 3
say coins + 2
```

### Loops

```ls
repeat 3 {
  say "Glow!"
}
```

### Conditionals

```ls
let coins = 5

if coins >= 5 {
  say "The gate opens!"
} else {
  say "You need more coins."
}
```

## Quest Flow

The current frontend uses a small fantasy quest line:

1. **Say Your Name**
   The map magician cannot see the learner until they create and say a name.

2. **Light the Lantern**
   The learner uses a repeat loop to light the path.

3. **Pay the Bridge Troll**
   The learner uses a conditional to check whether they have enough coins.

4. **Open the Gate**
   The board updates when the learner completes the quest chain.

## Tech Stack

### Language + Backend

- Python
- FastAPI
- Pydantic
- Pytest

### Frontend

- React
- TypeScript
- Vite
- CSS
- Canvas API

## Project Structure

```txt
little-syntax/
  little_syntax/
    ast_nodes.py
    lexer.py
    parser.py
    interpreter.py
    runner.py
    quest_checker.py
    api.py
  examples/
    hello.ls
    variables.ls
    math.ls
    conditionals.ls
    repeat.ls
  tests/
    test_say.py
    test_variables.py
    test_math.py
    test_conditionals.py
    test_repeat.py
    test_quest_checker.py
    test_api.py
  frontend/
    src/
      App.tsx
      App.css
      components/
        DragonIntro.tsx
        DragonIntro.css
```

## Running the Backend

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run the FastAPI server:

```bash
python3 -m uvicorn little_syntax.api:app --reload
```

Open the API docs:

```txt
http://127.0.0.1:8000/docs
```

## Running the Frontend

In a separate terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the local frontend:

```txt
http://localhost:5173/
```

## Running Tests

From the project root:

```bash
source .venv/bin/activate
python3 -m pytest
```

For the frontend:

```bash
cd frontend
npm run build
```

## API Example

Request:

```json
{
  "source": "let coins = 5\nsay coins + 2"
}
```

Response:

```json
{
  "output": ["7"],
  "errors": [],
  "variables": {
    "coins": 5
  }
}
```

## Why This Project Matters

Little Syntax is a systems-meets-education project. It combines language design, interpreter construction, API development, frontend design, accessibility-minded feedback, and playful learning design.

The project is intentionally built from the ground up to show how programming tools can be made more approachable for beginners.

## Roadmap

Planned improvements include:

- More quests and branching quest paths
- Stronger quest validation
- Syntax highlighting
- More visual board reactions when quests are completed
- Saved progress
- Additional beginner programming concepts
- Expanded documentation for the Little Syntax language

## Roadmap

- [x] Set up project structure
- [x] Milestone 1: `say` command
- [x] Milestone 2: variables with `let`
- [x] Milestone 3: numbers and math
- [x] Milestone 4: conditionals with `if` / `else`
- [x] Milestone 5: loops with `repeat`
- [x] Milestone 6: quest checker prototype
- [x] Milestone 7: web playground
- [x] Milestone 8: FastAPI Backend
- [x] Milestone 9: Add Frontend
