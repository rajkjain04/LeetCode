class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals = sorted(intervals)
        
        for i in range(0, len(intervals) - 1):
            current_end_time = intervals[i][1]
            next_start_time = intervals[i + 1][0] 
            
            if current_end_time > next_start_time:
                return False 
            
        return True 
        