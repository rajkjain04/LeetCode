class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visit = set() 
        numberOfIslands = 0 
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def isValid(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit or grid[r][c] == "0":
                return False 

            return True  

        def dfs(r, c):
            stack = []
            stack.append((r, c))

            while stack: 
                r, c = stack.pop()

                if (r, c) in visit:
                    continue 
                
                visit.add((r, c))

                for dx, dy in directions:
                    nr, nc = r + dx, c + dy 
                    if isValid(nr, nc):
                        stack.append((nr, nc)) 

        for r in range(0, rows):
            for c in range(0, cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    numberOfIslands += 1 
                    dfs(r, c)

        return numberOfIslands





        