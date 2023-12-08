class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        array_sum=sum(nums)
        total=0
        while n>=0:
            total+=n
            n-=1
        return total-array_sum
                    