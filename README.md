<div align="center">

# 🐍 Python Module 08 - The Matrix

**Mastering Python Environments, Dependencies & Secure Configuration**

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Code Style](https://img.shields.io/badge/code%20style-flake8-black)](https://flake8.pycqa.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Exercises](#-exercises)
  - [ex0: Entering the Matrix](#ex0-entering-the-matrix)
  - [ex01: Loading Programs](#ex01-loading-programs)
  - [ex02: Accessing the Mainframe](#ex02-accessing-the-mainframe)
- [Testing](#-testing)
- [Code Quality](#-code-quality)

---

## 🎯 Overview

This module explores essential Python development practices including:

- 🔧 Virtual environment detection and management
- 📦 Dependency management with pip and Poetry
- 🔐 Secure configuration with environment variables
- 📊 Data analysis with NumPy, Pandas, and Matplotlib

## 📁 Project Structure

```
PythonModule08/
├── ex0/
│   └── construct.py          # Virtual environment detector
├── ex01/
│   ├── loading.py            # Dependency validator & data analyzer
│   ├── requirements.txt      # pip dependencies
│   └── pyproject.toml        # Poetry configuration
├── ex02/
│   ├── oracle.py             # Environment configuration loader
│   ├── .env.example          # Example configuration template
│   └── .gitignore            # Git ignore rules
└── README.md
```

> **Note:** This project uses `ex01/` and `ex02/` naming convention (zero-padded) as per chapter guidelines.

## 🔧 Prerequisites

- **Python** 3.10 or higher
- **flake8** for code linting

## 🚀 Quick Start

### 1. Create Virtual Environment

```bash
python3 -m venv matrix_env
source matrix_env/bin/activate  # On macOS/Linux
# or
matrix_env\Scripts\activate     # On Windows
```

### 2. Install Dependencies

```bash
# For ex01
pip install -r ex01/requirements.txt

# For ex02
pip install python-dotenv
```

### 3. Run Code Quality Checks

```bash
flake8 ex0 ex01 ex02
```

---

## 📚 Exercises

### ex0: Entering the Matrix

**File:** `ex0/construct.py`

Detects whether Python is running inside a virtual environment and displays contextual information.

#### 🎯 Learning Objectives

- Distinguish between `sys.prefix` and `sys.base_prefix`
- Identify the active Python interpreter
- Understand virtual environment activation
- Locate package installation paths

#### 🏃 Usage

```bash
# Global environment
python3 ex0/construct.py

# Virtual environment
matrix_env/bin/python ex0/construct.py
```

---

### ex01: Loading Programs

**Files:** `ex01/loading.py`, `ex01/requirements.txt`, `ex01/pyproject.toml`

Validates dependencies, demonstrates pip vs Poetry workflows, and performs data analysis with visualization.

#### 🎯 Learning Objectives

- Graceful dependency handling
- Compare `requirements.txt` (pip) vs `pyproject.toml` (Poetry)
- Display installed package versions
- Generate data visualizations with Matplotlib

#### 🏃 Usage

```bash
# Without dependencies (shows installation instructions)
python3 ex01/loading.py

# With dependencies installed
matrix_env/bin/pip install -r ex01/requirements.txt
matrix_env/bin/python ex01/loading.py
```

---

### ex02: Accessing the Mainframe

**Files:** `ex02/oracle.py`, `ex02/.env.example`, `ex02/.gitignore`

Loads configuration from environment variables and `.env` files using `python-dotenv`, validates required settings, and reports configuration status.

#### 🎯 Learning Objectives

- Load `.env` files for development
- Understand environment variable precedence
- Avoid hardcoded secrets
- Proper `.gitignore` usage for sensitive files

#### 🏃 Usage

```bash
# Without configuration (shows missing keys)
python3 ex02/oracle.py

# With .env file
cp ex02/.env.example ex02/.env
matrix_env/bin/pip install python-dotenv
matrix_env/bin/python ex02/oracle.py

# With environment override
MATRIX_MODE=production \
DATABASE_URL=postgresql://zion/db \
API_KEY=secret123 \
LOG_LEVEL=INFO \
ZION_ENDPOINT=https://zion.example/api \
matrix_env/bin/python ex02/oracle.py
```

---

## 🧪 Testing

### Run All Tests

```bash
# Lint all exercises
flake8 ex0 ex01 ex02

# Test ex0
python3 ex0/construct.py
matrix_env/bin/python ex0/construct.py

# Test ex01
python3 ex01/loading.py
matrix_env/bin/python ex01/loading.py

# Test ex02
python3 ex02/oracle.py
matrix_env/bin/python ex02/oracle.py
```

## 🎨 Code Quality

This project follows PEP 8 style guidelines enforced by `flake8`:

```bash
flake8 ex0 ex01 ex02
```

---

<div align="center">

**Made with ☕ and 🐍**

[Report Bug](../../issues) · [Request Feature](../../issues)

</div>
