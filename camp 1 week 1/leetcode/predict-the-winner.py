class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def rec(start,end):
            if start == end:
                return nums[start]
            score_one = nums[start] - rec(start + 1, end)
            score_two = nums[end] - rec(start, end - 1)

            return max(score_one, score_two)

        return rec(0, len(nums) - 1) >= 0