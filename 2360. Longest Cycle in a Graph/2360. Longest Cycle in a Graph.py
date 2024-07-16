from typing import List


def longestCycle(self, edges: List[int]) -> int:
    comprimento = -1
    time = 1
    timeVisited = [0] * len(edges)

    for i in range(len(edges)):
        if timeVisited[i]:
            continue
        startTime = time
        u = i
        while u != -1 and not timeVisited[u]:
            timeVisited[u] = time
            time += 1
            u = edges[u]  # Mover para o próximo nó
        if u != -1 and timeVisited[u] >= startTime:
            comprimento = max(comprimento, time - timeVisited[u])

    return comprimento
