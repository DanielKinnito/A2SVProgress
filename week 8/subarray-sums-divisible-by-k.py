class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        prefix_sums_freq = {0: 1}

        for num in nums:
            prefix += num
            temp = prefix % k

            if temp in prefix_sums_freq:
                count += prefix_sums_freq[temp]

            if temp in prefix_sums_freq:
                prefix_sums_freq[temp] += 1
            else:
                prefix_sums_freq[temp] = 1

        return count