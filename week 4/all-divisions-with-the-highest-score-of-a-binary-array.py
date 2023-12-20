class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # Hint 1 - maintain the number of zeros and ones on the left side
        total_zeros = nums.count(0)
        total_ones = len(nums) - total_zeros

        result = [0]
        left_zeros = 0
        left_ones = 0
        max_score = total_ones

        for i, num in enumerate(nums):
            left_zeros += num == 0
            left_ones += num == 1
            # Hint 2 - calculate the number of ones on the right side
            right_ones = total_ones - left_ones
            # Hint 3 - calculate the division score using left_zeros and right_ones
            score = left_zeros + right_ones

            if max_score == score:
                result.append(i + 1)
            
            elif max_score < score:
                max_score = score
                result = [i + 1]

        return result