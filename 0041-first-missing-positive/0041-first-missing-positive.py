class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)
        
        j = 1 
        
        for item in sorted_nums:
            if item == j:
                j += 1 
                
            elif item > j:
                return j 
                
        
        return j 
            