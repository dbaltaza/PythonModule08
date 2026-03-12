# Python Module 08 - The Matrix

This repository contains three exercises about Python environments,
dependency management, and secure configuration.

## Project Structure

- `ex0/construct.py`
- `ex01/loading.py`
- `ex01/requirements.txt`
- `ex01/pyproject.toml`
- `ex02/oracle.py`
- `ex02/.env.example`
- `ex02/.gitignore`

Note: Some briefs write `ex1/` and `ex2/`, while chapter exercise names use
`ex01/` and `ex02/`. This project follows chapter naming.

## Requirements

- Python 3.10+
- `flake8`

Optional local virtual environment:

```bash
python3 -m venv matrix_env
```

## Exercise Summary

### ex0 - Entering the Matrix

`construct.py` detects if Python is running in a virtual environment and prints
different status blocks for global vs isolated execution.

Key concepts:

- `sys.prefix` vs `sys.base_prefix`
- Current interpreter path
- Activation instructions
- Virtual environment package path

### ex01 - Loading Programs

`loading.py` validates dependencies, explains pip vs Poetry usage, runs a small
data analysis using `numpy` + `pandas`, and generates a chart with
`matplotlib`.

Key concepts:

- Graceful handling of missing dependencies
- `requirements.txt` (pip) and `pyproject.toml` (Poetry)
- Package version visibility

### ex02 - Accessing the Mainframe

`oracle.py` loads settings from environment variables and `.env` using
`python-dotenv`, checks required keys, and reports security/config status.

Key concepts:

- `.env` loading for development
- Environment variable override behavior
- Avoiding hardcoded secrets
- `.env` in `.gitignore`

## Validation Commands

Run from repository root:

```bash
flake8 ex0 ex01 ex02
```

### ex0 tests

```bash
python3 ex0/construct.py
matrix_env/bin/python ex0/construct.py
```

### ex01 tests

Without dependencies:

```bash
python3 ex01/loading.py
```

With dependencies in virtual env:

```bash
matrix_env/bin/pip install -r ex01/requirements.txt
matrix_env/bin/python ex01/loading.py
```

### ex02 tests

Without configuration:

```bash
python3 ex02/oracle.py
```

With `.env` file:

```bash
cp ex02/.env.example ex02/.env
matrix_env/bin/pip install python-dotenv
matrix_env/bin/python ex02/oracle.py
```

With environment override:

```bash
MATRIX_MODE=production \
DATABASE_URL=postgresql://zion/db \
API_KEY=secret123 \
LOG_LEVEL=INFO \
ZION_ENDPOINT=https://zion.example/api \
matrix_env/bin/python ex02/oracle.py
```
