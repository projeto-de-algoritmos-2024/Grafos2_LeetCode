import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Criação da lista de adjacência
        adj = {i: [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                d = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([d, j])
                adj[j].append([d, i])

        resp = 0
        visited = set()
        min_heap = [[0, 0]]  # Lista de prioridades com o custo inicial 0

        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            resp += cost
            visited.add(i)
            for cost_neighbor, neighbor in adj[i]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, [cost_neighbor, neighbor])

        return resp

# Exemplo de uso:
solution = Solution()
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(solution.minCostConnectPoints(points))  # Output esperado: 20
