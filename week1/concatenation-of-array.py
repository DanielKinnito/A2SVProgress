class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l = n * 2
        answer = [0] * l
        for i in range(n):
            answer[i] = nums[i]
            answer[i + n] = nums[i]
        return answer