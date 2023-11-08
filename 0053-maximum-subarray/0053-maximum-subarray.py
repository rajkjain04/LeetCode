class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        prevSum = 0 
        maxSum = nums[0]
        
        L = 0 
        R = 0 
        
        while R <= len(nums) - 1:
            prevSum += nums[R] 
            maxSum = max(prevSum, maxSum)
            
            if prevSum < 0:
                prevSum = 0 
                L = R + 1 
                
            R += 1 
            
        return maxSum 
            
