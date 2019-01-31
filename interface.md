## Interface with abstract base class

```python
import abc

# This is our `interface` that needs to be extended. Remember, base
# classes cannot be instantiate directly - they need to be extended.

class Bird(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        pass

#  TypeError: Can't instantiate abstract class Bird with abstract
#  methods fly
#  bird = Bird()
#  bird.fly()

class Parrot(Bird):
    def fly(self):
        print('flying parrot')

parrot = Parrot()
parrot.fly()
```
