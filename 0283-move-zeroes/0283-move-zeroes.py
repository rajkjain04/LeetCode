class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        L = 0 
        R = 1 
        
        while R <= len(nums) - 1:
            
            if nums[L] == 0 and nums[R] != 0:
                nums[L] = nums[R] 
                nums[R] = 0 
                L += 1 
            
            elif nums[L] != 0:
                L += 1 
                    
            R += 1 
    