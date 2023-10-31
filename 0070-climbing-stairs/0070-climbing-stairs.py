class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {}
        
        def helper(i, n, cache):
            
            if i == n:
                return 1 
            
            if i > n:
                return 0 
            
            if i in cache:
                return cache[i]
            
            left = helper(i + 1, n, cache)
            right = helper(i + 2, n, cache)
            
            cache[i] = left + right 
            
            return cache[i]
        
        return helper(0, n, cache)
            
        
        
        
         
        