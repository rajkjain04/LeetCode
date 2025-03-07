class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        tag = 0 
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue 
            
            if nums[i] > nums[i - 1] and tag == -1:
                return False 
            
            if nums[i] < nums[i - 1] and tag == 1:
                return False 
            
            if nums[i] > nums[i - 1]:
                tag = 1 
            
            else:
                tag = -1 
        
        return True 
        