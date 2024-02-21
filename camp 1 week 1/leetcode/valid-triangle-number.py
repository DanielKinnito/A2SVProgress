class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        n = len(nums)

        start, end = 0, n - 2
        for i in range(n - 1, -1, -1):
            end = i - 1
            while start < end:
                if nums[i] < nums[start] + nums[end]:
                    answer += end - start
                    end -= 1
                else:
                    start += 1
            start = 0
        
        return answer