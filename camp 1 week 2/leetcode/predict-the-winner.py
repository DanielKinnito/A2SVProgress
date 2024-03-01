class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # return True
        def solve(left, right):
            if left == right:
                return nums[left]
            
            left_score = nums[left] - solve(left + 1, right)
            right_score = nums[right] - solve(left, right - 1)

            return max(left_score, right_score)
        return solve(0, len(nums) - 1) >= 0