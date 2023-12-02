# With

Basic context manager.

```python
class Foo(object):
    def __init__(self):
        self.count = 0

    def __enter__(self):
        self.count += 1
        return self.count

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("EXIT", self.count)


with Foo() as foo:
    print(f"GOT {foo}")
    raise Exception("foo")
    print("end")
```

## With Contextlib

```python
from contextlib import contextmanager


@contextmanager
def hello(name):
    try:
        print("enter")
        yield name
    finally:
        print("exit")


with hello("world") as h:
    print("GOT", h)
    raise Exception("error")
```
