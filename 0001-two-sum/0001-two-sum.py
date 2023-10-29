class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {} 
        output = [] 
        
        for i in range(len(nums)):
            value = target - nums[i] 
            
            if value in hash_map:
                output.append(hash_map[value])
                output.append(i)
                
                return output 
            
            else: 
                hash_map[nums[i]] = i 
                
                
        
                
                
            
        
        