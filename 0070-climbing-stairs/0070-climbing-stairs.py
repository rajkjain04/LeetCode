class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        cache = {} 
        
        # Using Recursion        
        def dfs(i, n, cache):
            
            if i > n:
                return 0 
            
            if i == n:
                return 1 
            
            if i in cache:
                return cache[i]
            
            left = dfs(i + 1, n, cache)
            right = dfs(i + 2, n, cache)
            
            cache[i] = left + right 
            
            return cache[i]
        
        return dfs(0, n, cache)
            
            
            
        
        
        
         
        