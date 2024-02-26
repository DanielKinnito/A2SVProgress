class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        length = len(nums)

        prefix = [0] * length
        prefix[0] = nums[0]

        for i in range(1, length):
            prefix[i] = prefix[i - 1] + nums[i]
        
        running_avg = prefix[0]
        answer = running_avg

        for i in range(1, length):
            denominator = i + 1
            running_avg = ceil(prefix[i]/denominator)
            answer = max(answer, running_avg)

        return answer