class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set() 
        numberOfIslands = 0 
        
        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS) or ((r, c) in visit or grid[r][c] == "0"):
                return 
            
            visit.add((r, c))
            
            down = dfs(r + 1, c)
            up = dfs(r - 1, c)
            right = dfs(r, c + 1)
            left = dfs(r, c - 1)
            
        for r in range(0, ROWS):
            for c in range(0, COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    numberOfIslands += 1 
                    dfs(r, c)
            
        return numberOfIslands 
            
        
        
        
        
        
        