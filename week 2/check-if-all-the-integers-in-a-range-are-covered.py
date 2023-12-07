class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        #adding elements of the ranges in to one set
        check_set = { j for arr in ranges for j in range(arr[0], arr[1] + 1)}

        #adding elements between ranges of left and right
        ranges_set = {arr for arr in range(left, right + 1)}

        #checking if the second is the subset of the first
        return ranges_set <= check_set