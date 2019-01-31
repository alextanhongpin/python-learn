# Module importing


Structure:
```
/mod1
  /__init__.py
  /greet.py
/mod2
  /__init__.py
  /greet.py
main.py
```

`main.py`:

```python
# main.py
import mod1
from mod2 import greet

mod1.greet()
greet.greet()
```

The `__init__.py` for `mod1`:

```python
import mod1.greet as greeter

def greet():
    print('super greet')
    greeter.greet()
```

`mod1.py`:

```python
def greet():
    print('from mod1')
```

`mod2.py`:

```python
def greet():
    print('from mod2')
```
