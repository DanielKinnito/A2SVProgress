class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        stack = []
        next_greater = [-1] * length

        for i in range(length * 2):
            while stack and nums[stack[-1]] < nums[i % length]:
                next_greater[stack.pop()] = nums[i % length]
            stack.append(i % length)
        
        return next_greater