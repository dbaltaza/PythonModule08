import os
import site
import sys


def is_inside_virtual_environment() -> bool:
    """
    Detect if the current interpreter is running in a virtual environment.

    Detection logic:
    - `sys.prefix` points to the active environment.
    - `sys.base_prefix` points to the base/global Python installation.
    - In a virtual environment, `sys.prefix != sys.base_prefix`.
    - Older virtualenv setups may expose `sys.real_prefix`.
    """
    try:
        base_prefix: str = getattr(sys, "base_prefix", sys.prefix)
        real_prefix = getattr(sys, "real_prefix", None)
        return bool(real_prefix) or sys.prefix != base_prefix
    except Exception:
        return False


def get_global_site_packages_path() -> str:
    """Return an expected global site-packages path based on base_prefix."""
    try:
        base_prefix: str = getattr(sys, "base_prefix", sys.prefix)
        if os.name == "nt":
            return os.path.join(base_prefix, "Lib", "site-packages")
        version = f"python{sys.version_info.major}.{sys.version_info.minor}"
        return os.path.join(base_prefix, "lib", version, "site-packages")
    except Exception:
        return "Could not determine global package path."


def get_current_site_packages_path() -> str:
    """Return site-packages path for the currently running interpreter."""
    try:
        paths: list[str] = site.getsitepackages()
        if paths:
            return paths[0]
    except Exception:
        pass
    try:
        return site.getusersitepackages()
    except Exception:
        return "Could not determine current package path."


def print_outside_matrix_status() -> None:
    """Print output for runs outside a virtual environment."""
    try:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")
        print("\nThen run this program again.")
    except Exception as error:
        print(f"Error while printing outside status: {error}")


def print_inside_construct_status() -> None:
    """Print output for runs inside a virtual environment."""
    try:
        env_name: str = os.path.basename(sys.prefix)
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print("\nPackage installation path:")
        print(get_current_site_packages_path())
    except Exception as error:
        print(f"Error while printing inside status: {error}")


def main() -> None:
    """Program entry point."""
    try:
        if is_inside_virtual_environment():
            print_inside_construct_status()
        else:
            print_outside_matrix_status()
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
