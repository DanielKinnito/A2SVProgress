class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        placeholder = -1

        for seeker in range(len(nums)):
            if nums[seeker] != 0:
                placeholder += 1
                
                nums[seeker], nums[placeholder] = nums[placeholder], nums[seeker]