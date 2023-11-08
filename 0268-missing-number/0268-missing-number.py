class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.append(0) 
        output = 0 
        
        for i in range(len(nums)):
            output ^= i ^ nums[i]
            
        return output 
            