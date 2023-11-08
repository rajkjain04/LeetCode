class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        unique = set() 
        longestSequence = 0 
        
        for item in nums:
            if item not in unique:
                unique.add(item)
                
        for i in range(0, len(nums)):
            
            newSequence = 0 
            
            if nums[i] - 1 not in unique:
                newSequence += 1
                item = nums[i]
                while item + 1 in unique:
                    newSequence += 1 
                    item += 1 
                    
                longestSequence = max(longestSequence, newSequence)
                
        return longestSequence 
        