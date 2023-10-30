class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set() 
        queue = [] 
        
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r, c))
        
        def isValid(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit) or (rooms[r][c] == -1 or rooms[r][c] == 0):
                return False 
            
            return True 
        
        dist = 0 
        
        while queue:
            for i in range(len(queue)):
                r, c = queue.pop(0)
                rooms[r][c] = dist 
                neighbours = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                
                for nx, ny in neighbours:
                    if isValid(nx, ny):
                        visit.add((nx, ny))
                        queue.append((nx, ny))
            
            dist += 1 
                
                
                
            
            
            
            
            
            
            
            
            
            