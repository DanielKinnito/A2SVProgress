class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        length = len(colors)
        left = 0
        right = length - 1

        while colors[left] == colors[-1]:
            left += 1

        while colors[right] == colors[0]:
            right -= 1

        return max(length - 1 - left, right)