class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: 
        
        if not grid:
            return 0 
        
        islands = 0 
        ROWS, COLS = len(grid), len(grid[0])
        visit = set() 
        
        def isValid(r, c):
            
            if (r < 0 or r == ROWS or c < 0 or c == COLS) or (r,c) in visit or grid[r][c] == "0":
                return False 
                
            return True 
            
        def dfs(r, c):
            visit.add((r, c))
            stack = [] 
            
            stack.append((r, c))
                   
            while stack:
                r, c = stack.pop()
                neighbours = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

                for nx, ny in neighbours:
                    if isValid(nx, ny):
                        visit.add((nx, ny))
                        stack.append((nx, ny))
                
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    islands += 1 
                    dfs(r, c)
                    
        return islands 
        
            
        
        
        
        
        