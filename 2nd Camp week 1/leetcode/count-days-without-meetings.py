class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        
        merged = []
        for meeting in meetings:
            if not merged or meeting[0] > merged[-1][1]:
                merged.append(meeting.copy())
            else:
                merged[-1][1] = max(merged[-1][1], meeting[1])
        
        free_days = 0
        free_days += merged[0][0] - 1
        
        free_days += days - merged[-1][1]
        
        for i in range(1, len(merged)):
            gap = merged[i][0] - merged[i-1][1] - 1
            free_days += gap
        
        return free_days