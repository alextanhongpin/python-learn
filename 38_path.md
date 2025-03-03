# Creating new directory and file

```python
import pathlib


p = pathlib.Path("test")
p.exists() or p.mkdir()
p = p / "a.txt"

with open(p, "w") as f:
    f.write("Hello, World!\n")
```
