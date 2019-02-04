from collections import Counter

sentence = 'this is the best thing ever for the end'
counter = Counter(sentence.split(' '))
print(counter)
print(counter.most_common(3))
