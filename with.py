from contextlib import contextmanager


@contextmanager
def hello(name):
    try:
        print("enter")
        yield name
    finally:
        print("exit")


with hello("world") as h:
    print("GOT", h)
    raise Exceptiom("error")
