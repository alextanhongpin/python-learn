# Retry

Writing retry without using library like tenacity etc.


```python
def retry(func, max_attempts=5, exceptions=(Exception), backoff=lambda n: math.pow(2, n)):
  for i in range(max_attempts + 1):
     try:
        return func()
     except exceptions as e:
        if i == max_attempts:
          raise e
        time.sleep(backoff(i))
```
