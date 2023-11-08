class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        unique = set() 
        
        for item in nums:
            if item not in unique and item > 0:
                unique.add(item)
        
        i = 1 
        while i in unique:
            i += 1 
            
        return i 
        
        