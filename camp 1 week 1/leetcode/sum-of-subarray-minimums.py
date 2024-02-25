class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        answer = 0
        prev_less = [-1] * n
        next_less = [n] * n
        stack = []

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                index = stack.pop()
                next_less[index] = i
            if stack:
                prev_less[i] = stack[-1]
            stack.append(i)

        for i, num in enumerate(arr):
            answer += num * (i - prev_less[i]) * (next_less[i] - i)
            answer %= 1000000007

        return answer 