class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        output = [] 
        storage = {} 
        
        for i in range(0, len(nums)): 
            if nums[i] not in storage:
                storage[target-nums[i]] = i

            else: 
                output.append(i)
                output.append(storage[nums[i]])
                return output 
                
        
        return output 