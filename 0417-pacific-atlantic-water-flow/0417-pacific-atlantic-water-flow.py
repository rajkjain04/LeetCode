class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        visitedPacific = set() 
        visitedAtlantic = set() 
        
        output = [] 
          
        def isValid(r, c, prev_value, isPacific):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS):
                return False 
            
            if (isPacific and (r, c) in visitedPacific):
                return False 
            
            if(isPacific is False and (r, c) in visitedAtlantic):
                return False 
            
            if (heights[r][c] < prev_value):
                return False 
                
            return True
        
        def dfs(r, c, isPacific):
            stack = [(r, c)]
            
            while stack:
                r, c = stack.pop()
                prev_value = heights[r][c]
                
                if isPacific:
                    visitedPacific.add((r, c))
                    
                else:
                    visitedAtlantic.add((r, c))
                
                neighbours = [(r + 1,  c), (r - 1, c), (r, c + 1), (r, c - 1)]
                
                for nx, ny in neighbours:
                    if isValid(nx, ny, prev_value, isPacific):
                        stack.append((nx, ny))
                 
        # Pacific Top Border 
        for c in range(0, COLS):
            dfs(0, c, True)
            
            
        # Pacific Left Border 
        for r in range(1, ROWS):
            dfs(r, 0, True)
            
        # Atlantic Right Boundary
        for r in range(ROWS):
            dfs(r, COLS - 1, False)
            
        # Atlantic Bottom Boundary 
        for c in range(COLS):
            dfs(ROWS -1, c, False)
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visitedPacific and (r, c) in visitedAtlantic:
                    output.append([r, c])
        return output 
        
        
        
        
        
        