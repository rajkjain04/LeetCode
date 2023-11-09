class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        unique = set(arr) 
        
        last_number = arr[-1]
        
        final = 0 
        number = 0 
        i = 1
        
        while True:
            if i not in unique: 
                final += 1 
                number = i 
                
            if final == k:
                return number 
            
            i += 1
            
        return number 
        