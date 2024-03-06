class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # low = 0
        # high = len(nums) - 1

        # while low <= high:
        return bisect_left(nums, target)