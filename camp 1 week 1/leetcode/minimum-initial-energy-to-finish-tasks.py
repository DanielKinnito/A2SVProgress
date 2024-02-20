class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[1] - x[0], reverse = True)
        # print(tasks)
        answer = tasks[0][1]
        minimum = tasks[0][1]

        for task in tasks:
            if task[1] >= minimum:
                answer += task[1] - minimum
                minimum = task[1] - task[0]
            else:
                minimum -= task[0]
        return answer