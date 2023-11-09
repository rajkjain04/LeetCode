class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)
        
        j = 1
        
        for i in range(0, len(sorted_nums)):
            if sorted_nums[i] == j:
                j += 1 
            
            elif sorted_nums[i] > j:
                return j 
            
        return j 