from collections import ChainMap

d1 = {i: i for i in range(100)}
d2 = {i: i * i for i in range(100)}
c = ChainMap(d1, d2)
print(c[5], c.maps[0][5])

d1.update(d2)
print(c[5], c.maps[0][5])
