class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        res = 0 
        i = 0 
        
        intervals = sorted(intervals)
        
        last = intervals[0]
                
        for i in range(1, len(intervals)):
            current = intervals[i] 
            
            currentStart = current[0]
            currentEnd = current[1] 
            
            lastStart = last[0]
            lastEnd = last[1]
            
            if currentStart < lastEnd: 
                if currentEnd < lastEnd:
                    last = current 
                res += 1 
            
            else: 
                last = current 
            
        return res 
            
            
        
        
        
        
        