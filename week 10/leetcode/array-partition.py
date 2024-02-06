class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        n = len(nums)
        for i in range(0, (n) - 1, 2):
            answer += min(nums[i], nums[i + 1])
        return answer