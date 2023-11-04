class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == "":
            return 0 
        
        seen = set() 
        L = 0 
        R = 1 
        seen.add(s[L]) 
        maxLen = len(seen) 
        
        while R <= len(s) - 1: 
            if s[R] not in seen:
                seen.add(s[R])
                maxLen = max(len(seen), maxLen)
                R += 1 
                
            else: 
                maxLen = max(len(seen), maxLen) 
                while s[R] in seen: 
                    seen.remove(s[L]) 
                    L += 1 
        
        return maxLen 
                 