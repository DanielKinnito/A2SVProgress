class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        i = 0
        while i < len(nums):
            for j in range(nums[i]):
                answer.append(nums[i+1])
            i +=2
        return answer