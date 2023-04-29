# Exception


## Print better exceptions with loguru

```python
from itertools import combinations
from loguru import logger


@logger.catch
def division(a: int, b: int):
    return a / b

if __name__ == '__main__':
    division(5, 0)
```

## Error cause


We can wrap errors using the `YourError from e`:


```python
def run():
    raise Exception("bad input")


def value():
    try:
        run()
    except Exception as e:
        raise ValueError("value is invalid") from e


def main():
    try:
        value()
    except ValueError as e:
        print("ValueError:", e, "cause", e.__cause__)
    except Exception as e:
        print("Treated as Exception:", e)


main()
```

## ExceptionGroup

Allows you to handle deeply nested error, and handling specific cause _simulataneously_:


```python
def value():
    raise ExceptionGroup("value is invalid", [TypeError(1), ValueError(2)])


def main():
    try:
        value()
    except* ValueError as e:
        # This will execute.
        print('Treated as ValueError:', e)
    except* TypeError as e:
        # This will also execute!
        print('Treated as TypeError:', e)


main()

# Treated as ValueError: value is invalid (1 sub-exception)
# Treated as TypeError: value is invalid (1 sub-exception)
```
