## Interface with abstract base class

Annotations provides hints on the input params and return types too:

```python
import abc

# This is our `interface` that needs to be extended. Remember, base
# classes cannot be instantiate directly - they need to be extended.

class Bird(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        pass

    def type(self) -> str:
        pass

    def num_feathers(self, num: int):
        pass

#  TypeError: Can't instantiate abstract class Bird with abstract
#  methods fly
#  bird = Bird()
#  bird.fly()

class Parrot(Bird):
    def __init__(self, name):
        self._name = name

    def fly(self):
        print('flying parrot')
    def name(self):
        return self._name

    def num_feathers(self, num: int):
        print(f'{self._name} has {num} feathers')

parrot = Parrot('jake')
parrot.fly()
print(parrot.name())
parrot.num_feathers(100)

```
