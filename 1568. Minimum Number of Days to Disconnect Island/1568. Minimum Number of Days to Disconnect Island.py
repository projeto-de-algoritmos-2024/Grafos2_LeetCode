import collections
from typing import  List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def count_islands() -> int:
            directions = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

            visited = set()
            islands = 0

            def bfs(x, y):
                queue = collections.deque([(x, y)])
                visited.add((x, y))

                while queue:
                    cur_i, cur_j = queue.popleft()
                    for d in directions:
                        new_i = cur_i + d[0]
                        new_j = cur_j + d[1]
                        if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in visited and grid[new_i][new_j] == 1:
                            queue.append((new_i, new_j))
                            visited.add((new_i, new_j))

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        islands += 1
                        bfs(i, j)

            return islands

        m = len(grid)
        n = len(grid[0])

        # checar o numero inicial de islands
        initial_islands = count_islands()
        if initial_islands > 1:
            return 0

        # remove cada land cell e checar o numero de islands
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() > 1:
                        return 1
                    grid[i][j] = 1

        return 2
