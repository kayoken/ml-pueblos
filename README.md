# ML Pueblos

This is the accompanying Readme for the Pueblos Repository:


## Setup

The added [requirements.txt file](requirements.txt) contains all libraries and dependencies we need to execute.

### Unzip data.zip

1. go to src/
2. python3 unzip.py
3. check data in data/

### Run the Frontend

1. got to frontend/
2. streamlit frontend.py
3. App should be available under localhost:8501

## Python Installation

### **`macOS`** type the following commands : 


- Install the virtual environment and the required packages by following commands:

    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
### **`WindowsOS`** type the following commands :

- Install the virtual environment and the required packages by following commands.

   For `PowerShell` CLI :

    ```PowerShell
    pyenv local 3.11.3
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

    For `Git-Bash` CLI :
    ```
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/Scripts/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```