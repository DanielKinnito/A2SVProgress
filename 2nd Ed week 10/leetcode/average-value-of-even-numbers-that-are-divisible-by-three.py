class Solution:
    def averageValue(self, nums: List[int]) -> int:
        n = 0
        div = 0

        for num in nums:
            if num % 6 == 0:
                n += num
                div += 1

        if div == 0:
            return 0

        return n // div