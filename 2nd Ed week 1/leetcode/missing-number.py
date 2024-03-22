class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        index = 0
        while index < length:
            correct_idx = nums[index]
            if correct_idx == length:
                index += 1
            elif nums[index] != nums[correct_idx]:
                nums[index], nums[correct_idx] = nums[correct_idx], nums[index]
            else:
                index += 1
        print(nums)
        for i in range(length):
            if i != nums[i]:
                return i
        
        return length