class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = [] 
        time, fresh = 0, 0 
        
        ROWS, COLS = len(grid), len(grid[0])

        def isValid(r, c, grid):
            if (r < 0 or r == ROWS or c < 0 or c == COLS) or (grid[r][c] != 1):
                return False 
            
            return True 
                 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1 
                
                if grid[r][c] == 2:
                    queue.append((r, c))
                    
        while queue and fresh > 0:
            
            for i in range(len(queue)):
                row, col = queue.pop(0)
                
                neighbours = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
                
                for nx, ny in neighbours:
                    if isValid(nx, ny, grid):
                        grid[nx][ny] = 2 
                        queue.append((nx, ny))
                        fresh -= 1 
                
            time += 1 
                
        return time if fresh == 0 else -1 
                    
                    

                
                
            
            
        
        
        
        
        
        