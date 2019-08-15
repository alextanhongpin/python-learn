## Batching

Sample code to batch a list with python.

```python
def batch(items, batch_size):
	bucket = len(items) // batch_size 
	hi = 0
	for i in range(bucket):
		lo, hi = i * batch_size, (i+1) * batch_size
		yield items[lo:hi]
	if hi < len(items):
		yield items[hi:]

for item in batch([0]* 43, 20):
	print(item)
```
