class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        prevSum = 0 
        maxSum = nums[0]
        
        for n in nums:
            prevSum = max(prevSum, 0)
            prevSum += n  
            maxSum = max(maxSum, prevSum) 
            
        return maxSum 
        