class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        unique = set() 
        
        for item in nums:
            if item not in unique:
                unique.add(item)
                
                
        j = 1 
        
        while j in unique:
            j += 1 
        
        
        return j 
        