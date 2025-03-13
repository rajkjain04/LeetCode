class Solution:
    def firstUniqChar(self, s: str) -> int:

        hashMap = {}

        for i in range(0, len(s)):
            if s[i] not in hashMap:
                hashMap[s[i]] = (i, 1)
            
            else: 
                index, count = hashMap[s[i]]
                hashMap[s[i]] = (index, count + 1)
        
        minValue = float('inf')
        for key, value in hashMap.items():
            index, count = value
            if count != 1:
                continue 
            
            minValue = min(minValue, index)
        
        if minValue == float('inf'):
            return -1 

        return minValue
