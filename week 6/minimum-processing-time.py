class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()

        max_time = 0

        for i in range(len(tasks)):
            max_time = max(max_time, processorTime[i // 4] + tasks[i])

        return max_time