## K-Mean clustering

```python
from functools import reduce
import random
import math


# Takes out k-random elements of the data.
def generate_centroid(k, data=[]):
    return random.sample(data, k)


# Compute the euclidean distance between two vectors.
def distance(v, w):
    dist = 0
    for i in range(len(v)):
        dist += math.pow(v[i] - w[i], 2)
    return math.sqrt(dist)


# From all the centroids, find the closest one to the current vector.
def assign_centroid(v, centroids):
    return v, min(centroids, key=lambda centroid: distance(v, centroid))


def move_centroids(points, centroids):
    result = []
    for centroid in centroids:
        # Find all points with the given centroid.
        curr = [
            point for point, assigned_centroid in points
            if assigned_centroid == centroid
        ]

        # Get the average point.
        x, y = zip(*curr)
        size = len(curr) + 1
        result.append((sum(x) / size, sum(y) / size))
    return result


def k_mean(k, data):
    # We need a starting point - we can choose to purely randomised them, or we
    # can just sample some points from the existing ones.
    centroids = generate_centroid(k, data)

    # Termination criteria.
    best_weight = float('inf')
    while True:
        # For each point, assign the closest centroid to it.
        points_with_centroids = [
            assign_centroid(item, centroids) for item in data
        ]

        # Compute the distance score for that given centroids.
        weight = sum([
            distance(item, centroid)
            for item, centroid in points_with_centroids
        ])

        if weight < best_weight:
            best_weight = weight
        else:
            return points_with_centroids

        centroids = move_centroids(points_with_centroids, centroids)

    return data


data = [[1, 1], [2, 2], [1, 0], [5, 5], [6, 6], [7, 7]]
result = k_mean(3, data)

from collections import defaultdict

grouped = defaultdict(list)
for point, centroid in result:
    grouped[centroid].append(point)

for centroid, points in grouped.items():
    print(centroid, points)
```
