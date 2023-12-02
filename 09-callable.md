## Callable

```python
class Foo:
    def __call__(self, *args, **kwargs):
        print("I am called", args, kwargs)


f = Foo()
f("hello", msg="world")
```
