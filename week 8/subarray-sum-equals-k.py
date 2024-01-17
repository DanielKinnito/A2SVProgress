class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        prefix_sums_freq = {0: 1}  

        for num in nums:
            prefix += num
            if prefix - k in prefix_sums_freq:
                count += prefix_sums_freq[prefix - k]
            
            if prefix in prefix_sums_freq:
                prefix_sums_freq[prefix] += 1
            else:
                prefix_sums_freq[prefix] = 1

        return count
        # print(prefix_sums_freq)