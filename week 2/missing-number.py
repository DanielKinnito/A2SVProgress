class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_dict = {}
    
        # Populate the dictionary with the numbers in the array
        for num in nums:
            my_dict[num] = 1
        
        # Find the missing number
        for i in range(len(nums) + 1):
            if i not in my_dict:
                return i