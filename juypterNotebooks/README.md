# Jupyter Notebooks Directory

This directory contains a virtual Python environment and example Jupyter notebooks.

## Contents

- `example_notebook.ipynb` - Example notebook with calculations and visualizations
- `requirements.txt` - Python dependencies for the notebook
- `venv/` - Virtual Python environment

## Requirements

The virtual environment is already set up with:
- numpy - For numerical computations
- matplotlib - For plotting and visualization  
- pandas - For data manipulation
- jupyter - For running Jupyter notebooks

## How to Use

### Option 1: Open in VS Code
1. Open this folder in VS Code
2. The Jupyter extension should automatically use the venv
3. Open `example_notebook.ipynb` and run cells

### Option 2: Run Jupyter from command line
```bash
cd juypterNotebooks
venv\Scripts\jupyter.exe notebook
```

### Option 3: Run with a specific kernel
To register the virtual environment as a Jupyter kernel:
```bash
cd juypterNotebooks
venv\Scripts\python.exe -m ipykernel install --user --name=jupyter_env
```

Then start Jupyter:
```bash
venv\Scripts\jupyter.exe notebook
```

## Testing

The setup has been verified to work with:
- NumPy array operations
- Matplotlib plotting (sine/cosine functions)
- Pandas DataFrame operations

You can run the test script to verify:
```bash
venv\Scripts\python.exe -c "import numpy; import matplotlib; import pandas; print('All imports successful!')"