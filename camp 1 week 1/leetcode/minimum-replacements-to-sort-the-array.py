class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[n - 1]
        count = 0

        for i in range(n-2, -1, -1):
            steps = nums[i] // prev
            if nums[i] % prev != 0:
                steps += 1
                prev = nums[i] // steps
            count += steps - 1

        return count