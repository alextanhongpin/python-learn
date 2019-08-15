## Flattening objects recursive


```python
## Flatten
def flatten(obj, prev_key=''):
    result = {}
    for key in obj:
        newkey = f'{prev_key}.{key}' if prev_key else key
        if isinstance(obj[key], dict):
            res = flatten(obj[key], newkey)
            if res is not None:
                result.update(res)
        else:
            result[newkey] = obj[key]
    return result


print(flatten({
    'a': {
        'x': 100,
        'y': 200
    },
    'b': {
        'c': {
            'd': 100,
            'e': 200,
            'f': 300
        }
    }
}))
```
