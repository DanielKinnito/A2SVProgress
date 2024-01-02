class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < len(numbers) and right > -1:
            summation = numbers[left] + numbers[right]
            if summation > target:
                right -= 1
            if summation < target:
                left += 1
            
            if summation == target:
                return [left + 1, right + 1]