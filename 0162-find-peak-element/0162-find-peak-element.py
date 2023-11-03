class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0 
        
        l = 0 
        r = len(nums) - 1 
        
        while l <= r:
            m = (l + r) // 2 
            
            if m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1
                
            elif m > 0 and nums[m] < nums[m - 1]:
                r = m - 1
                
            else:
                return m 
                
            
            
            
            
            
            
        
                
                
                
        
        