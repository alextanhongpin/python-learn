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


## Custom context manager

```python
from dataclasses import dataclass 
from contextlib import ExitStack, contextmanager


@contextmanager
def read_file():
    print('reading file')
    yield 'hello world'
    print('file read complete')

@dataclass
class Session:
    def __init__(self, session):
        self.stack = ExitStack()
        self.session = session

    async def __aenter__(self):
        return self.stack.enter_context(read_file())

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.stack.close()

async def main():
    print('start session')
    async with Session('hello') as session:
        print('in session start')
        print(session)
        print('in session end')
    print('end session')
    print("hello world")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```
