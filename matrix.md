## Matrix multiplication with @

Only works with numpy array, for builtin, we need to implement them ourselves `object.__matmul__(self, other)`:

```python
import numpy as np

np.array([1, 2]) @ np.array([3, 4])
np.ones(3) @ np.eye(3)
```
