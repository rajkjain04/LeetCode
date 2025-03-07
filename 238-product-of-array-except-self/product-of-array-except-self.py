class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1] * len(nums)
        prefix = [] 
        postfix = [1] * len(nums) 
        totalPrefix = 1 
        totalPostfix = 1 

        for i in range(0, len(nums)):
            totalPrefix *= nums[i] 
            prefix.append(totalPrefix)
        
        for i in range(len(nums) - 1, -1 , -1):
            totalPostfix *= nums[i] 
            postfix[i] = totalPostfix   

        output[0] = postfix[1]
        output[-1] = prefix[-2]

        for i in range(1, len(output) - 1):
            output[i] = prefix[i - 1] * postfix[i + 1]
        
        return output
        

        
        
        