class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_C = 0
        cur_C = 0
        for i in nums:
            if i == 1:
                cur_C += 1
                max_C = max(max_C, cur_C)
            else:
                cur_C = 0
        return max_C