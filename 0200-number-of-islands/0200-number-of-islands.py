class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid: 
            return 0 
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set() 
        islands = 0 
        
        def isValid(r, c):
            
            if (r < 0 or r == ROWS or c < 0 or c == COLS) or (grid[r][c] == "0" or (r, c) in visit):
                return False
            
            return True 
            
        
        def bfs(r, c): 
            queue = [] 
            visit.add((r, c))
            queue.append((r, c))
            
            while queue:
                row, col = queue.pop(0) 
                neighbours = [(row - 1, col), (row + 1, col), (row, col + 1), (row, col- 1)]
                
                for nx, ny in neighbours:
                    if isValid(nx, ny):
                        queue.append((nx, ny))
                        visit.add((nx, ny))
                
        for r in range(0, ROWS):
            for c in range(0, COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1 
                    bfs(r, c)
        
        return islands 