import collections
from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def count():
            resp = 0

            visited = set()
            
            for i in range (m):
                for j in range (n):
                    if grid [i][j] == 1 and (i, j) not in visited:
                        resp += 1

                        queue = collections.deque([(i, j)])
                        visited.add((i, j))

                        while queue:
                            CurrentI, CurrentJ = queue.popleft()

                            for d in directions:
                                UpdateI = CurrentI + d[0]
                                UpdateJ = CurrentJ + d[1]

                                if 0 <= UpdateI < m and 0 <= UpdateJ < n and (UpdateI, UpdateJ) not in visited and grid[UpdateI][UpdateJ] == 1:
                                    queue.append((UpdateI, UpdateJ))
                                    visited.add((UpdateI, UpdateJ))

            return resp

        
        directions = [(-1, 0), (1,0), (0,-1), (0,1)]

        m = len(grid)
        n = len(grid[0])

        if count() > 1:
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count() > 1:
                        return 1

                    grid[i][j] = 1

        return 2
