class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(0, len(nums)):
            if nums[i] < 0:
                nums[i] = 0 
        
        for i in range(0, len(nums)):
            current_value = abs(nums[i])
            index = current_value - 1 
            
            if index < 0 or index > len(nums) - 1:
                continue 
                
            value_at_index = nums[index]
            if value_at_index != 0:
                if value_at_index > 0:
                    nums[index] = -value_at_index
            
            else:
                nums[index] = -(len(nums) + 1)
        
        j = 1 
        
        for i in range(0, len(nums)):
            if nums[i] >= 0:
                return j 
            
            j += 1 
        
        return j 
        