import importlib
import sys


REQUIRED_MODULES: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computations ready",
    "matplotlib": "Visualization ready",
    "requests": "Network access ready",
}


def load_module(module_name: str) -> object | None:
    """Load a module by name and return it or None when unavailable."""
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None
    except Exception as error:
        print(f"[ERROR] Unexpected import failure for {module_name}: {error}")
        return None


def check_dependencies() -> tuple[dict[str, object], list[str]]:
    """Check required dependencies and report statuses."""
    loaded_modules: dict[str, object] = {}
    missing_modules: list[str] = []
    print("Checking dependencies:")
    for module_name, ready_message in REQUIRED_MODULES.items():
        module = load_module(module_name)
        if module is None:
            print(f"[MISSING] {module_name} - Install required")
            missing_modules.append(module_name)
        else:
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {module_name} ({version}) - {ready_message}")
            loaded_modules[module_name] = module
    return loaded_modules, missing_modules


def print_install_help() -> None:
    """Print installation instructions for pip and Poetry."""
    try:
        print("\nMissing dependencies detected.")
        print("Install with pip:")
        print("pip install -r requirements.txt")
        print("\nInstall with Poetry:")
        print("poetry install")
        print("poetry run python loading.py")
    except Exception as error:
        print(f"[ERROR] Could not print install help: {error}")


def print_manager_comparison() -> None:
    """Explain pip vs Poetry usage in a compact runtime message."""
    try:
        print("\nDependency management mode:")
        print("- pip: installs from requirements.txt")
        print("- Poetry: installs from pyproject.toml with lock support")
    except Exception as error:
        print(f"[ERROR] Could not print manager comparison: {error}")


def build_matrix_dataframe(
    np_module: object,
    pd_module: object,
) -> object | None:
    """Create a simulated dataset for matrix analysis."""
    try:
        point_count: int = 1000
        signal = np_module.random.normal(
            loc=50.0,
            scale=10.0,
            size=point_count,
        )
        trend = np_module.linspace(0, 15, point_count)
        noise = np_module.random.normal(loc=0.0, scale=4.0, size=point_count)
        output = signal + trend + noise

        dataframe = pd_module.DataFrame(
            {
                "cycle": np_module.arange(1, point_count + 1),
                "signal": signal,
                "trend": trend,
                "output": output,
            }
        )
        return dataframe
    except Exception as error:
        print(f"[ERROR] Failed to build matrix dataset: {error}")
        return None


def save_visualization(plt_module: object, dataframe: object) -> bool:
    """Generate and save a matrix analysis plot."""
    try:
        plt_module.figure(figsize=(10, 5))
        plt_module.plot(
            dataframe["cycle"],
            dataframe["output"],
            label="Matrix Output",
            color="green",
            linewidth=1.2,
        )
        plt_module.title("Matrix Signal Analysis")
        plt_module.xlabel("Cycle")
        plt_module.ylabel("Output")
        plt_module.legend()
        plt_module.grid(True, alpha=0.25)
        plt_module.tight_layout()
        plt_module.savefig("matrix_analysis.png", dpi=130)
        plt_module.close()
        return True
    except Exception as error:
        print(f"[ERROR] Failed to create visualization: {error}")
        return False


def run_analysis(modules: dict[str, object]) -> bool:
    """Run matrix data analysis and render visualization."""
    try:
        pandas_module = modules["pandas"]
        numpy_module = modules["numpy"]
        modules["matplotlib"]
    except KeyError as error:
        print(f"[ERROR] Missing loaded module key: {error}")
        return False
    except Exception as error:
        print(f"[ERROR] Failed to access loaded modules: {error}")
        return False

    print("\nAnalyzing Matrix data...")
    dataframe = build_matrix_dataframe(numpy_module, pandas_module)
    if dataframe is None:
        return False

    try:
        point_count = int(dataframe.shape[0])
        avg_output = float(dataframe["output"].mean())
        max_output = float(dataframe["output"].max())
        print(f"Processing {point_count} data points...")
        print(f"Average output: {avg_output:.2f}")
        print(f"Maximum output: {max_output:.2f}")
    except Exception as error:
        print(f"[ERROR] Failed during statistics computation: {error}")
        return False

    pyplot_module = load_module("matplotlib.pyplot")
    if pyplot_module is None:
        print("[ERROR] matplotlib.pyplot is unavailable.")
        return False

    print("Generating visualization...")
    if not save_visualization(pyplot_module, dataframe):
        return False

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
    return True


def main() -> None:
    """Program entry point."""
    try:
        print("LOADING STATUS: Loading programs...")
        loaded_modules, missing_modules = check_dependencies()
        if missing_modules:
            print_install_help()
            sys.exit(1)

        print_manager_comparison()
        if not run_analysis(loaded_modules):
            sys.exit(1)
    except SystemExit:
        raise
    except Exception as error:
        print(f"[ERROR] Unexpected failure: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
