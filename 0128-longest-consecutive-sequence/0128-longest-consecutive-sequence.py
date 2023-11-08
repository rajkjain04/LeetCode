class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        unique = set() 
        longestSequence = 0 
        
        for item in nums:
            if item not in unique:
                unique.add(item)
                
        for item in unique:
            newSequence = 0 
            if item - 1 not in unique:
                newSequence += 1
                while item + 1 in unique:
                    newSequence += 1 
                    item += 1 
                    
                longestSequence = max(longestSequence, newSequence)
                
        return longestSequence 
        