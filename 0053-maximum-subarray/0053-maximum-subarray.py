class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        L = 0
        R = 0 
        
        maxSum = nums[0] 
        prevSum = 0 
        
        while R <= len(nums) - 1:
            prevSum += nums[R] 
            
            maxSum = max(maxSum, prevSum) 
            
            if prevSum < 0: 
                L = R 
                prevSum = 0 
                
            R += 1 
            
        return maxSum 
            
        