## Sample Repository

Folder structure:

```
/repository
  /__init__.py
  /car.py
/main.py
```

`car.py`:
```python
import abc

class Repository(abc.ABC):
    @abc.abstractmethod
    def get_car(self):
        pass
```

`main.py`:
```python
from repository.car import Repository

class CarRepoImpl(Repository):
    def get_car(self):
        print('getting car')

def get_car(repo: Repository):
    repo.get_car()

car_repo = CarRepoImpl()
get_car(car_repo)
```
