import os
import nbformat
from pathlib import Path
from nbconvert.preprocessors import ExecutePreprocessor

# Get the script's directory and then reference the notebooks directory relative to it
script_dir = Path(__file__).resolve().parent
path = script_dir.parent / "notebooks/1_cleaning_and_eda"

def run_all_notebooks(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith(".ipynb"):
            notebook_path = os.path.join(folder_path, file)
            print(f"Running notebook: {notebook_path}")
            run_notebook(notebook_path)


def run_notebook(notebook_path):
    with open(notebook_path, encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
        ep.preprocess(nb, {"metadata": {"path": os.path.dirname(notebook_path)}})
        with open(notebook_path, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)


if __name__ == "__main__":
    run_all_notebooks(path)