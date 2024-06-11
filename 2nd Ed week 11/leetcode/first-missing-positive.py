class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()

        answer = 1
        for num in nums:
            if num <= 0:
                continue
            else:
                if num > answer:
                    return answer
                else:
                    answer += 1
        return answer