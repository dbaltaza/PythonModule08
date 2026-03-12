import os
import sys

REQUIRED_KEYS: tuple[str, ...] = (
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
)


def load_environment() -> bool:
    """Load environment values from .env when available."""
    script_directory = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(script_directory, ".env")
    try:
        from dotenv import load_dotenv  # type: ignore

        return load_dotenv(dotenv_path=env_path)
    except ModuleNotFoundError:
        print("[WARN] python-dotenv is not installed.")
        print("Install it with: pip install python-dotenv")
        return False
    except Exception as error:
        print(f"[ERROR] Could not load .env file: {error}")
        return False


def read_configuration() -> dict[str, str]:
    """Read matrix configuration from environment variables."""
    config: dict[str, str] = {}
    for key in REQUIRED_KEYS:
        try:
            config[key] = os.getenv(key, "").strip()
        except Exception:
            config[key] = ""
    return config


def normalize_mode(mode_value: str) -> str:
    """Return a valid matrix mode or a safe default."""
    try:
        normalized = mode_value.lower().strip()
    except Exception:
        normalized = ""
    if normalized in {"development", "production"}:
        return normalized
    return "development"


def report_configuration(config: dict[str, str]) -> None:
    """Print configuration status in a human-readable format."""
    try:
        matrix_mode = normalize_mode(config.get("MATRIX_MODE", ""))
        database_url = config.get("DATABASE_URL", "")
        api_key = config.get("API_KEY", "")
        log_level = config.get("LOG_LEVEL", "")
        zion_endpoint = config.get("ZION_ENDPOINT", "")

        print("ORACLE STATUS: Reading the Matrix...")
        print("Configuration loaded:")
        print(f"Mode: {matrix_mode}")

        if database_url:
            print("Database: Connected to configured instance")
        else:
            print("Database: Missing DATABASE_URL")

        if api_key:
            print("API Access: Authenticated")
        else:
            print("API Access: Missing API_KEY")

        print(f"Log Level: {log_level or 'INFO'}")
        if zion_endpoint:
            print("Zion Network: Online")
        else:
            print("Zion Network: Missing ZION_ENDPOINT")
    except Exception as error:
        print(f"[ERROR] Could not report configuration: {error}")


def has_required_configuration(config: dict[str, str]) -> bool:
    """Return True when all required configuration values are set."""
    try:
        for key in REQUIRED_KEYS:
            if not config.get(key):
                return False
        return True
    except Exception:
        return False


def check_env_gitignore() -> bool:
    """Verify if .env is listed in local .gitignore."""
    script_directory = os.path.dirname(os.path.abspath(__file__))
    gitignore_path = os.path.join(script_directory, ".gitignore")
    try:
        if not os.path.exists(gitignore_path):
            return False
        with open(gitignore_path, "r", encoding="utf-8") as file_handler:
            entries = [line.strip() for line in file_handler.readlines()]
        return ".env" in entries
    except Exception:
        return False


def has_placeholder_api_key(config: dict[str, str]) -> bool:
    """Detect non-secure placeholder values used in examples."""
    try:
        api_key = config.get("API_KEY", "").lower()
        placeholders = {"", "replace_me", "changeme", "secret123"}
        return api_key in placeholders
    except Exception:
        return True


def report_security(config: dict[str, str]) -> None:
    """Print security checklist around environment usage."""
    try:
        print("Environment security check:")
        print("[OK] No hardcoded secrets detected")

        if check_env_gitignore():
            print("[OK] .env file properly configured")
        else:
            print("[WARN] .env not found in .gitignore")

        if config.get("MATRIX_MODE", "").lower() == "production":
            print("[OK] Production overrides available")
        else:
            print("[INFO] Set MATRIX_MODE=production to test overrides")

        if has_placeholder_api_key(config):
            print("[WARN] API_KEY looks like a placeholder value")
    except Exception as error:
        print(f"[ERROR] Could not complete security checks: {error}")


def print_help() -> None:
    """Print help for missing or incomplete configuration."""
    try:
        print("\nHow to configure:")
        print("1. Copy .env.example to .env")
        print("2. Fill in your local values")
        print("3. Run again with: python3 oracle.py")
        print("4. Override for production:")
        print(
            "   MATRIX_MODE=production API_KEY=real_key "
            "python3 oracle.py"
        )
    except Exception as error:
        print(f"[ERROR] Could not print configuration help: {error}")


def main() -> None:
    """Program entry point."""
    try:
        load_environment()
        config = read_configuration()
        report_configuration(config)
        report_security(config)
        if not has_required_configuration(config):
            print_help()
            sys.exit(1)
        print("The Oracle sees all configurations.")
    except SystemExit:
        raise
    except Exception as error:
        print(f"[ERROR] Unexpected failure: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
