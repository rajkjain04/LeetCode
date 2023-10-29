class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        full_set = set() 
        current_set = set() 
        output = [] 
        
        for i in range(1, len(nums) + 1):
            full_set.add(i) 
            
        for j in range(len(nums)):
            current_set.add(nums[j])
            
        for item in full_set:
            if item not in current_set:
                output.append(item)

        return output 
            
        