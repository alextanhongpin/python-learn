# Retry

Writing retry without using library like tenacity etc.


```python
def retry(func, max_attempts=5, exceptions=(Exception)):
  sleep = 1
  for i in range(max_attempts + 1):
     try:
        return func()
     except exceptions as e:
        if i == max_attempts:
          raise e
        sleep *= 2
        time.sleep(sleep)
```
