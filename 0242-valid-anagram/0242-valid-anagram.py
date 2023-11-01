class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False 
        
        storage = {} 
        
        for i in range(len(s)):
            if s[i] not in storage:
                storage[s[i]] = 1 
                
            else:
                storage[s[i]] += 1 
                
        for j in range(len(t)):
            if t[j] not in storage:
                return False 
            
            else:
                storage[t[j]] -= 1 
                
        for key, value in storage.items():
            if value != 0:
                return False 
            
        return True 
            
            
        