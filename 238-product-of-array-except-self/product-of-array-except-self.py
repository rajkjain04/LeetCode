class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1 
        postfix = 1 
        output = [1] * len(nums)

        for i in range(0, len(nums) - 1):
            prefix *= nums[i]
            output[i + 1] = prefix 
        
        for j in range(len(nums) - 1, 0, -1):
            postfix *= nums[j]
            output[j - 1] *= postfix
        
        return output
                