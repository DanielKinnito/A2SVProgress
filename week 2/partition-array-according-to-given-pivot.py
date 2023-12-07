class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        result = []

        for num in nums:
            if num < pivot:
                result.append(num)

        for num in nums:
            if num == pivot:
                result.append(num)

        for num in nums:
            if num > pivot:
                result.append(num)

        return result