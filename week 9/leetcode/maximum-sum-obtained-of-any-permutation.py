class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0] * n

        for start, end in requests:
            count[start] += 1
            if end + 1 < n:
                count[end + 1] -= 1

        prefix = [0] * n
        prefix[0] = count[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + count[i]

        prefix.sort(reverse=True)
        nums.sort(reverse=True)

        result = sum(prefix[i] * nums[i] for i in range(n)) % (10**9 + 7)

        return result