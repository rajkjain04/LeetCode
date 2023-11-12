class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        output = [] 
        
        if intervals == []: 
            return [newInterval]
        
        elif newInterval[0] <= intervals[0][0]:
            intervals.insert(0, newInterval)
            
        elif newInterval[0] >= intervals[-1][0]:
            intervals.insert(len(intervals), newInterval)
             
        else: 
            for i in range(0, len(intervals) - 1): 
                currStart = intervals[i][0] 
                nextStart = intervals[i + 1][0] 
                newIntervalStart = newInterval[0]

                if currStart <= newIntervalStart <= nextStart: 
                    intervals.insert(i + 1, newInterval) 
                    break 
        
        output = [intervals[0]] 
        
        for i in range(1, len(intervals)):
            current = intervals[i] 
            start = current[0] 
            end = current[1] 
            lastEnd = output[-1][1]
            
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
                
            else:
                output.append(current)
    
        return output 
        
        