class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        hash_map = {} 
        
        for item in s:
            if item not in hash_map: 
                hash_map[item] = 1 
                
            else:
                hash_map[item] += 1 
        
        number = hash_map[s[0]]
        
        for key, value in hash_map.items():
            if value != number:
                return False 
        
        return True 
    