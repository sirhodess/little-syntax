# Little Syntax Setup Notes

## Local Development Setup

Create a virtual environment from the project root:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install project dependencies:

```bash
python3 -m pip install -r requirements.txt
```

## Python Alias Note

On this machine, `python` may be aliased to a global Python installation. To make sure dependencies install into the project virtual environment, use:

```bash
python3 -m pip install -r requirements.txt
```

or call the virtual environment Python directly:

```bash
.venv/bin/python -m pip install -r requirements.txt
```

## Run the API

Start the FastAPI server:

```bash
python3 -m uvicorn little_syntax.api:app --reload
```

Open the API docs:

```txt
http://127.0.0.1:8000/docs
```

## Run Tests

```bash
python3 -m pytest
```
