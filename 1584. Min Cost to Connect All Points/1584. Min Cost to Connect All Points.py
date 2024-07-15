import collections
from typing import List

def minCostConnectPoints(self, points: List[List[int]]) -> int:
    n = len(points)

    a = {i:[] for i in range(n) }

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i +1, n):
            x2, y2 = points[j]
            d = abs(x1-x2) + abs(y1-y2)
            a[i].append([d, j])
            a[j].append([d, i])


    resp = 0
    visited = set()
    min =[[0, 0]]

    while len(visited) < n:
        cost, i = heapq.heappop(min)
        if i in visited:
            continue
        resp += cost
        visited.add(i)
        for costNeighbor, neighbor in  [i]:
            if neighbor not in visited:
                heapq.heappush(min, [costNeighbor, neighbor])

    return resp