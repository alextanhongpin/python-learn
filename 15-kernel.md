# Kernel for Jupyter Notebook

```python
import sys
!echo {sys.executable}
# The output should be local to your directory.
# /Users/alextanhongpin/Documents/python/ortools-learn/.venv/bin/python
```

Run this (or poetry equivalent):
```python
!python -m pip install ipykernel
!python -m ipykernel install --user
```
