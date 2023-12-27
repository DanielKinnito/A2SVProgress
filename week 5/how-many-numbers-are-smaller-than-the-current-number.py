class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n

        for i in range(n):
            count = 0
            for j in range(n):
                if nums[j] < nums[i] and j != i:
                    count += 1
            answer[i] = count
        
        return answer