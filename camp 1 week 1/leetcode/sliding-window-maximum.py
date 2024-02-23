class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        queue = deque()
        answer = []

        for i in range(k):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        answer.append(nums[queue[0]])

        for right in range(k, length):
            while queue and queue[0] <= right - k:
                queue.popleft()
            while queue and nums[right] >= nums[queue[-1]]:
                queue.pop()
            queue.append(right)
            answer.append(nums[queue[0]])

        return answer