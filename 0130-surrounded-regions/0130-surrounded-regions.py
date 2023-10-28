class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        visit = set() 
        
        def isValid(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS) or (r, c) in visit or board[r][c] == "X":
                return False 
            
            return True 
        
        def dfs(r, c):
            stack = [(r, c)]
            
            while stack:
                r, c = stack.pop() 
                neighbours = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                
                for nx, ny in neighbours:
                    if isValid(nx, ny):
                        visit.add((nx, ny))
                        stack.append((nx, ny))
                        board[nx][ny] = "T"
            
        
        # Need to traverse the corners of the board 
        # Top border
        for c in range(COLS):
            if board[0][c] == "O":
                board[0][c] = "T"
                dfs(0, c)
        
        # Right border 
        for r in range(1, ROWS):
            if board[r][COLS - 1] == "O":
                board[r][COLS - 1] = "T"
                dfs(r, COLS - 1)
        
        # Bottom border 
        for c in range(COLS - 2, -1, -1):
            if board[ROWS - 1][c] == "O":
                board[ROWS - 1][c] = "T" 
                dfs(ROWS - 1, c)
        
        # Left border 
        for r in range(ROWS - 2, 0, -1):
            if board[r][0] == "O":
                board[r][0] = "T" 
                dfs(r, 0)
        
        
        # Final - Convert "T" to "O" and "O" to "X"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                    
                elif board[r][c] == "O":
                    board[r][c] = "X"
        
        