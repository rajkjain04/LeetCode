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
            cache[i + 1] = left
            right = helper(i + 2, cache)
            cache[i + 2] = right
            
            return left + right 
        
        return helper(0, cache)
            
            
            