class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()

        max_time = 0

        for i in range(len(tasks)):
            # calculate in intervals of 4
            max_time = max(max_time, processorTime[i // 4] + tasks[i])

        return max_time