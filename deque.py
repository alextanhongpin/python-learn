from collections import deque, defaultdict
d = deque([1, 2, 3, 4, 5])
d.rotate(2)
print(d)

text = 'hello world'
counts = {}
counts2 = defaultdict(int)
for word in text.split():
    word = word.lower().strip()
    counts2[word] += 1
    try:
        counts[word] += 1
    except KeyError:
        counts[word] = 1
print(counts, counts2)
