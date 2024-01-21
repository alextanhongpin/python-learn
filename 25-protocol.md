# Protocol

```python
from typing import Protocol

class SupportsClose(Protocol):
    def close(self) -> None:
        ...

# This function accepts any object that has a close method.
def close_resource(resource: SupportsClose) -> None:
    resource.close()

class Resource:
    def close(self):
        print("Resource closed")

# Usage:
r = Resource()
close_resource(r)  # Prints: Resource closed
```


## Another example

```python
from typing import Protocol


class Repository(Protocol):
    # Note that protocal can't define default value
    def create(self):
        pass


class UserRepository:
    def create(self) -> None:
        print("create user")


def create(repository: Repository) -> None:
    repository.create()


create(UserRepository())
```

## Abc

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def shared(self):
        print("shared")


class Triangle(Shape):
    def area(self):
        print("triangle area")


triangle = Triangle()
triangle.area()
triangle.shared()
```
