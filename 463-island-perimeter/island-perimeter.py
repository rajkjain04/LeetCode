class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        visit = set() 
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i, j):
            stack = [] 
            stack.append((i, j))
            islandPerimeter = 0 

            while stack:
                i, j = stack.pop()

                if (i, j) in visit:
                    continue 
                
                visit.add((i, j))
                
                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    if ni < 0 or ni >= rows or nj < 0 or nj >= cols or grid[ni][nj] == 0:
                        islandPerimeter += 1 
                    
                    elif (ni, nj) not in visit:
                        stack.append((ni, nj))
            
            return islandPerimeter 
            
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == 1:
                    return dfs(i, j)


        return 0 