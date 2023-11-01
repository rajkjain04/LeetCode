class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = {} 
        output = [] 
        
        for s in strs:
            
            count = [0] * 26 
            
            for i in s:
                value = ord(i) - ord('a') 
                count[value] += 1 
                
            tup = tuple(count)
            
            if tup not in hash_map:
                hash_map[tup] = [s]
                
            else:
                hash_map[tup].append(s)
                
        for key, value in hash_map.items():
            output.append(value)
            
        return output
                
            
            
            
            
            
            
            