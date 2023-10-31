class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = {} 
        
        def helper(i, cache): 
            
            if i >= len(nums):
                return 0 
            
            if i in cache:
                return cache[i]
            
            left = nums[i] + helper(i + 2, cache)
            right = helper(i + 1, cache)
            
            cache[i] = max(left, right)
            
            return cache[i]
        
        return helper(0, cache)
            