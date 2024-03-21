class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        length = len(nums)

        index = 0
        while index < length:
            correct_idx = nums[index] - 1

            if nums[index] != nums[correct_idx]:
                nums[index], nums[correct_idx] = nums[correct_idx], nums[index]
            else:
                index += 1
        
        answer = []
        for i in range(length):
            if nums[i] - 1 != i:
                answer.append(nums[i])
        
        return answer