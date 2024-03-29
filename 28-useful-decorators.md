# Useful decorators

List of useful decorators in python.

## atexit

Registers a function to be executed at program termination.

This function can be used to perform any task when the program is about to exit, whether it is due to normal execution or an unhandled exception.

```python
import atexit


@atexit.register
def exit_handler():
    print("exiting the program")


def main():
    print("inside the main program")
    raise ValueError("sth happened")


if __name__ == "__main__":
    main()
```

Output:
```
python3 playground.py
inside the main program
exiting the program
```

## unique enums

```python
from enum import Enum, unique


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)

try:
    # Attempt to create non-unique enum values.
    # This will raise an error because the value 1 is
    # already assigned to RED.
    @unique
    class RGB(Enum):
        RED = 1
        GREEN = 1
        BLUE = 3

except ValueError as e:
    print(e)
```

Output:
```
python3 playground.py
Color.RED
duplicate values found in <enum 'RGB'>: GREEN -> RED
```

## @singledispatch


The `@singledispatch` decorator is used to create generic functions in Python. It allows you to define a function that can have different implementations based on the type of the first argument.

Any type not implemented will call the original function.

```python
from functools import singledispatch


@singledispatch
def display_info(info):
    print("generic: {}".format(info))


@display_info.register(int)
def display_int(arg):
    print("Received an integer: {}".format(arg))


@display_info.register(str)
def display_str(arg):
    print("Received a string: {}".format(arg))


@display_info.register(Exception)
def display_exc(arg):
    print("Received an exception: {}".format(arg))


display_info(1)
display_info("one")
display_info(ValueError("hello"))
display_info([1, 2])
```

Output:

```
Received an integer: 1
Received a string: one
Received an exception: hello
generic: [1, 2]
```


## Others

Other useful decorators
- @classmethod
- @staticmethod
- @property
