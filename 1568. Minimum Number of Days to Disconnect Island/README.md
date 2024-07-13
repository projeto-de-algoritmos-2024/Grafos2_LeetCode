# 1568. Minimum Number of Days to Disconnect Island

You are given ```n m x``` n binary ```grid```  where ```1``` represents land and ```0``` represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of ```1```'s.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell ```(1)``` into a water cell ```(0)```.

Return the minimum number of days to disconnect the grid.


# Example 1:

![](https://github.com/user-attachments/assets/2b724a8d-c18d-4cec-a7e0-ae5abe205dc6)<br>

Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.

# Example 2:

![](https://github.com/user-attachments/assets/e40cafaa-60ee-4ad6-9e04-571d40651c5f)<br>

Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
 

# Constraints:

*  ```m == grid.length```

*  ```n == grid[i].length```

*  ```1 <= m, n <= 30```
 
*  ```grid[i][j] is either 0 or 1.```