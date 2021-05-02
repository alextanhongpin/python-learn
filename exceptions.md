# Print better exceptions with loguru
```python
from itertools import combinations
from loguru import logger


@logger.catch
def division(a: int, b: int):
    return a / b

if __name__ == '__main__':
    division(5, 0)
```
