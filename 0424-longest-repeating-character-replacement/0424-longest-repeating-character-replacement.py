class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        L = 0 
        R = 1 
        res = 0 
        
        if s[L] == s[R]:
            count = {s[L]: 2}
            
        else:
            count = {s[L]: 1, s[R]: 1}
        
        
        while R <= len(s) - 1:
            winLen = R - L + 1
            
            if (winLen - max(count.values()) <= k):
                res = max(res, winLen)
                R += 1
                if R <= len(s) - 1 and s[R] not in count:
                    count[s[R]] = 1 
                
                elif R <= len(s) - 1:
                    count[s[R]] += 1 
                
                else:
                    break
                
            else:
                count[s[L]] -= 1 
                L += 1 
                    
                
        return res                 
                
            
            
            
            
            
            
            
        
        
            
            
            
            
        
        
        