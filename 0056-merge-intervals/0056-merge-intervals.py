class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals) 
        output = [intervals[0]] 
        
        for i in range(1, len(intervals)):
            lastEnd = output[-1][1] 
            start = intervals[i][0]
            end = intervals[i][1]
            
            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd) 
                
            else:
                output.append([start, end])
                
        return output 
            

        