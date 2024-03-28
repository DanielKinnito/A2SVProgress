class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        factor_count = {}
        count = 0

        for num in nums:
            factor = gcd(num, k)
            want = k // factor

            for key in factor_count:
                if factor * key % k == 0:
                    count += factor_count[key]

            factor_count[factor] = factor_count.get(factor, 0) + 1

        return count