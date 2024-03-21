class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)

        index = 0
        while index < length:
            correct_idx = nums[index] - 1

            if nums[index] != nums[correct_idx]:
                nums[index], nums[correct_idx] = nums[correct_idx], nums[index]
            else:
                index += 1
        
        for i in range(length):
            if nums[i] - 1 != i:
                return nums[i]