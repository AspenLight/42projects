import sys
import os


def ft_inconstruct() -> None:
    pythpath = sys.executable
    venv = os.path.basename(sys.prefix)
    envpath = sys.prefix
    instpath = (f"{sys.prefix}/lib/python{sys.version_info[0]}."
                f"{sys.version_info[1]}/site-packages")
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {pythpath}")
    print(f"Virtual Environment: {venv}")
    print(f"Environment Path: {envpath}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")
    print("Package installation path:")
    print(instpath)


def ft_outconstruct() -> None:
    pythpath = sys.executable
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {pythpath}")
    print("Virtual Environent: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")


if __name__ == "__main__":
    if (hasattr(sys, 'real_prefix')
            or (hasattr(sys, 'base_prefix')
                and sys.base_prefix != sys.prefix)):
        ft_inconstruct()
    else:
        ft_outconstruct()
