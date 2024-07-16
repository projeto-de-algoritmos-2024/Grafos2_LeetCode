class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Criação da lista de adjacência pra armazenar as distâncias entre os pontos
        adj = {i: [] for i in range(n)}


        # Calcula a distância entre cada par de pontos e armazena na lista de adjacência
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                d = abs(x1 - x2) + abs(y1 - y2) # calcula a distância entre i e j
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


solution = Solution()
points = [[3,12],[-2,5],[-4,1]]
print(solution.minCostConnectPoints(points))  
