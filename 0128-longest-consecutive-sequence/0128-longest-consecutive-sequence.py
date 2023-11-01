class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        unique = set() 
        longest_consecutive = 0 
        
        for item in nums:
            if item not in unique:
                unique.add(item)
        
        print(unique)
        
        for item in unique:
            sequence_count = 1 
            if item - 1 in unique and item + 1 not in unique:
                while item - 1 in unique:
                    sequence_count += 1 
                    item -= 1 
                
            longest_consecutive = max(longest_consecutive, sequence_count)
            
            
        return longest_consecutive
        