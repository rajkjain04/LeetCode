class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        leftPointer = 0 
        rightPointer = 0 
        result = 0 
        count = {} 
        
        while rightPointer < len(s):
            # Get the length of the window
            windowLength = rightPointer - leftPointer + 1 

            if s[rightPointer] not in count: 
                count[s[rightPointer]] = 1 

            else:
                count[s[rightPointer]] += 1

            # Get the most frequent count in the HashMap
            mostFrequentCount = max(count.values())

            if windowLength - mostFrequentCount <= k:
                result = max(result, windowLength)

            else: 
                count[s[leftPointer]] -= 1 
                leftPointer += 1 
            
            rightPointer += 1 
            
        return result 
        