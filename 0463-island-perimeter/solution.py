class Solution(object):
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for x in range(rows)]
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return 1
            if grid[i][j] == 0:
                return 1
            if visited[i][j]:
                return 0
            
            visited[i][j] = True
            
            perimeter = 0
            perimeter += dfs(i+1, j)
            perimeter += dfs(i-1, j)
            perimeter += dfs(i, j+1)
            perimeter += dfs(i, j-1)
            
            return perimeter
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    return dfs(x, y)
