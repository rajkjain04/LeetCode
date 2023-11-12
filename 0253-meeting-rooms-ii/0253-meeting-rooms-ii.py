class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        startTimes = [] 
        endTimes = [] 
        
        for i in range(len(intervals)):
            startTimes.append(intervals[i][0])
            
        for i in range(len(intervals)):
            endTimes.append(intervals[i][1])
        
        startTimes = sorted(startTimes)
        endTimes = sorted(endTimes) 
        
        L = 0
        R = 0  
        count = 0 
        maxCount = 0 
        
        while L <= len(startTimes) - 1:
            if startTimes[L] < endTimes[R]:
                count += 1 
                L += 1 
                
            else:
                count -= 1 
                R += 1 
                
            maxCount = max(count, maxCount)
            
        return maxCount
                
            