# List

## Find first item

```
n = [1,2,3,4]

next(x for x in n if x > 2) # 3
next(x for x in n if x > 10) # raises StopIteration
next((x for x in n if x > 10), None) # Returns default
```
