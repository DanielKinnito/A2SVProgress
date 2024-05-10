class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        answer = -1
        seen = set()

        for num in nums:
            if -num in seen:
                answer = max(answer, abs(num))
            else:
                seen.add(num)

        return answer