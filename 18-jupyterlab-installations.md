# Jupyterlab


Warnings:

```
/Users/alextanhongpin/Documents/python/python-google-gemini/.venv/lib/python3.11/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html
  from .autonotebook import tqdm as notebook_tqdm
```

Solution:
```
pip install ipywidgets
```

## Dependencies Issue

```
  • Check your dependencies Python requirement: The Python requirement can be specified via the `python` or `markers` properties

    For fastembed, a possible solution would be to set the `python` property to ">=3.11,<3.12"
```
Solution:

Update the `pyproject.toml` file:

```
[tool.poetry.dependencies]
python = ">=3.11,<3.12"
```
