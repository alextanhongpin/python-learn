```python
from enum import IntEnum


class Colors(IntEnum):
    RED = 0
    GREEN = 1
    BLUE = 2


# Does not work if use Enum only, need IntEnum
print(list(map(int, Colors)))
print(list(Colors.__members__.keys()))
print(list(Colors.__members__.values()))
# [0, 1, 2]
# ['RED', 'GREEN', 'BLUE']
# [<Colors.RED: 0>, <Colors.GREEN: 1>, <Colors.BLUE: 2>]


a = (1, 2)
b = (2, 3)
print(a + b)
print(len(a))

for i in a:
    print(i)
def add_tuple(a, b):
    return tuple(map(sum, zip(a, b)))
    # res = []
    # for i in range(len(a)):
        # res.append(a[i] + b[i])
    # return tuple(res)

print(add_tuple(a, b))


x, y = 3, 5

print([(i, j) for i in range(x) for j in range(y)])
print([[1 if j == 0 else 0 for j in range(x)] for i in range(y)])


matrix = [[0] * x for i in range(y)]
print(matrix)
matrix[y-1][x-1] = 100
print(matrix)



coords = [(0, 0), (0, 1), (0, 0)]
pieces = ['P', '+', '-']

obs = dict(list(zip(coords, pieces))[::-1])
print(obs)
```
