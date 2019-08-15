## Counting words

```python
from collections import Counter

sentence = 'this is the best thing ever for the end'
counter = Counter(sentence.split(' '))
print(counter)
print(counter.most_common(3))
```

## Anagram

```python
from collections import Counter


def check_anagram_optimized(cnt1, arr1):
    if len(cnt1) != len(arr1):
        return False
    return cnt1 == Counter(arr1)


def find_anagrams(dictionaries, word):
    arr1 = Counter(word)
    return [
        item for item in dictionaries if check_anagram_optimized(arr1, item)
    ]


dictionary = [
    'friend', 'redfin', 'abcsde', 'refind', 'friende', 'asdasdsa', 'asdgadgad'
]

print(find_anagrams(dictionary, 'friend'))
```
