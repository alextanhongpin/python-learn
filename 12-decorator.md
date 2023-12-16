# Decorator
#
The functools module in Python is often used with decorators for a couple of reasons:

- Preserving function metadata with functools.wraps: When you create a decorator, it can obscure the metadata of the original function (like its name, docstring, etc.). If you use functools.wraps in your decorator, it will copy over this metadata from the original function to the new one.

- Creating decorator factories with functools.partial: If you want to create a decorator with arguments (also known as a decorator factory), functools.partial can be useful. It allows you to fix a certain number of arguments of a function and generate a new function.

Here's an example of using functools.wraps:

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
```

In this example, the wrapper function will have the same name, docstring, and module as the original func.

## Allowing custom parameters

To allow custom parameters for decorators in Python, you need to create a decorator factory. This is a function that returns a decorator. Here's a step-by-step plan:

1. Define a function that takes the custom parameters. This is the decorator factory.
2. Inside the decorator factory, define the decorator function. This function should take a single argument, which is the function to be decorated.
3. Inside the decorator function, define the wrapper function. This function will replace the original function.
4. Inside the wrapper function, you can add code before and after the call to the original function.
5. The decorator function should return the wrapper function.
6. The decorator factory should return the decorator function.

Here's the Python code that follows the above plan:

```python
def my_decorator_factory(param1, param2):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Something is happening before the function is called. Param1: {param1}, Param2: {param2}")
            func(*args, **kwargs)
            print("Something is happening after the function is called.")
        return wrapper
    return my_decorator

@my_decorator_factory("Hello", "World")
def my_function():
    print("Inside the function.")
```
