class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {}
        
        def helper(i, cache):
            
            if i == n:
                return 1 
            
            if i > n:
                return 0 
            
            if i in cache:
                return cache[i]
            
            left = helper(i + 1, cache)
            right = helper(i + 2, cache)
            cache[i] = left + right
            
            return cache[i]
        
        return helper(0, cache)
            
            
            