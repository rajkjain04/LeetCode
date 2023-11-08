class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        unique = set() 
        
        for item in nums:
            unique.add(item) 
            
        for i in range(len(nums) + 1):
            if i not in unique:
                return i 
        