# Using method as contextmanager 


```python
from contextlib import contextmanager

def todo(ctx = {}):
    ctx['dirty'] = True
    return ctx

class Greet:
    def __init__(self):
        self.data = {}
    @contextmanager
    def hello(self):
        try:
            yield self.data
            print(self.data)
        finally:
            print('done')


greet = Greet()
with greet.hello() as data:
    data['what'] = True

print(greet.data)

# print(todo(None))
print(todo())
ctx = todo({})
print(ctx)
ctx['name'] = 'john'
print(todo(ctx))
print(todo())
```
