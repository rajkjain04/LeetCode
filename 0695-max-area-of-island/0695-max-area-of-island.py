class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0 
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        max_area = 0 
        
        def isValid(r,c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS) or (r, c) in visit or grid[r][c] == 0:
                return False 
            
            return True 
        
        def dfs(r, c):
            area = 0
            stack = [(r, c)] 
            
            while stack: 
                r, c = stack.pop() 
                
                neighbours = [(r - 1, c), (r + 1, c),  (r, c - 1), (r, c + 1)]
                
                for nx, ny in neighbours:
                    if isValid(nx, ny):
                        visit.add((nx, ny))
                        area += 1 
                        stack.append((nx, ny))
            
            return area 
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    visit.add((r, c))
                    area = 1 + dfs(r, c) 
                    max_area = max(area, max_area)
                    
        return max_area 
                    
                    
                    
        