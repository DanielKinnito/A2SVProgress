class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        index = 0
        while index < length:
            correct_idx = nums[index] - 1
            if correct_idx == length:
                index += 1
            elif nums[index] != nums[correct_idx]:
                nums[index], nums[correct_idx] = nums[correct_idx], nums[index]
            else:
                index += 1
        
        answer = []
        for i in range(length):
            if i != nums[i] - 1:
                answer.append(i + 1)

        return answer