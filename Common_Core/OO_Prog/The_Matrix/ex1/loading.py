import importlib as il


def imp_module(name: str, description: str) -> bool:
    try:
        module = il.import_module(name)
        print(f"[OK] {name} ({module.__version__}) - {description}")
        return True
    except ModuleNotFoundError:
        print(f"[KO] {name} is not installed")
        return False


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    if (not imp_module("pandas", "Data manipulation ready") or
            not imp_module("numpy", "Numerical computation ready") or
            not imp_module("requests", "Network access ready") or
            not imp_module("matplotlib", "Visualization ready")):
        print("Missing dependencies.")
        print("To install with pip:\npip install -r requirements.txt")
        print("To install with poetry:\npoetry install"
              "\npoetry run python loading.py")
    else:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt

        data = np.random.randint(0, 100, size=1000)
        frame = pd.DataFrame({"data": data})
        print("\nAnalyzing Matrix data...")
        print("Processing 1000 data points...")
        print("Generating visualization...\n")
        plt.figure()
        plt.plot(frame["data"])
        plt.title("Plotted Data")
        plt.savefig("matrix_analysis.png")
        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")
