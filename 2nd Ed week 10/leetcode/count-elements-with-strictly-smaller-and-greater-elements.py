class Solution:
    def countElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = list(set(nums))
        nums.sort()

        answer = 0
        for i in range(1, len(nums)-1):
            answer += count[nums[i]]
        
        return answer