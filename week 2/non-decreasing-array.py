class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        non_decreasing_count = 0
        
        # Check if the array is non-decreasing
        for num in range(1, len(nums)):
            if nums[num] < nums[num - 1]:
                non_decreasing_count += 1
                if num > 1 and nums[num] < nums[num - 2]:
                    # Adjust the current element to make the array non-decreasing
                    nums[num] = nums[num - 1]
                else:
                    # Adjust the previous element to make the array non-decreasing
                    nums[num - 1] = nums[num]
                    
        # If the count is greater than 1, that means we found multiple instances of peaks in the array
        return non_decreasing_count <= 1
            
        # [5,7,1,8]
        # if non_decreasing:
        #     count+=1
        #     if num > prevprevnum

