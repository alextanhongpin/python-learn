# Working with enums

```python
from enum import Enum
from enum import IntEnum

# Enum of colors red, green and blue.
# Making it as a subclass of int, we can compare it with int values.
class Color(int, Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED == 1)

# But better to use IntEnum
class Shapes(IntEnum):
    CIRCLE = 1
    SQUARE = 2


print(Shapes.CIRCLE == 1)
# print(Shapes(10) in Shapes) # Will raise exception.

# Check if the number 1 is a valid enum value of Shapes.
print(1 in list(Shapes))
print(10 in list(Shapes))
```
