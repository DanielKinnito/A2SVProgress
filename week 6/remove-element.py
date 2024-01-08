class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        answer = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[answer] = nums[i]
                answer += 1

        return answer