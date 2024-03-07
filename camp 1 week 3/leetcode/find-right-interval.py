class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # return []
        length = len(intervals)
        answer = [-1] * length
        
        interval_dictionary = {}

        check_intervals = []
        for index, interval in enumerate(intervals):
            check_intervals.append(interval[0])
            if interval[0] in interval_dictionary:
                interval_dictionary[interval[0]] = index
            else:
                interval_dictionary[interval[0]] = index
        
        check_intervals.sort()
 
        for i in range(length):
            temp = bisect_left(check_intervals, intervals[i][1])

            if temp > length - 1 or temp < 0:
                answer[i] = -1
            else:
                answer[i] = interval_dictionary[check_intervals[temp]]
        
        return answer