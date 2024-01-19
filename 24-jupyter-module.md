# Module

In Jupyter notebook, you can use a python module by simply importing it:

```python
# greet.py

def hello():
    print('hello world')
```

In the notebook:
```
import greet
greet.hello()
```

## Making changes

However, when you make changes, you will realised the notebook will complain the attributes are not found.

To solve it, you need to reload the module:

```
import example
import importlib

# make changes to example.py file

importlib.reload(example)
```
