## Positional-only and Keyword-only Arguments in Python

```python
def foo(a, b, /, *args, c="some_required_default_value", **kwargs):
    print(a, b, args, c, kwargs)
```

All values before `/` must be positional only.

All values after the `*` must be keyword only.
