class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        before = [num for num in nums if num < pivot]
        after = [num for num in nums if num > pivot]
        between = [num for num in nums if num == pivot]

        result = []

        for i in range(len(before)):
            result.append(before[i])
        for i in range(len(between)):
            result.append(between[i])
        for i in range(len(after)):
            result.append(after[i])

        return result