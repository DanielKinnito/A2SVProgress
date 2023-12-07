class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive = [num for num in nums if num > 0]
        negative = [num for num in nums if num < 0]

        result = []
        length = len(nums)

        for i in range(length/2):
            result.append(positive[i])
            result.append(negative[i])
        
        return result