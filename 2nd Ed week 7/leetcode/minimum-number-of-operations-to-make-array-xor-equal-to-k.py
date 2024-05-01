class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        def find_ones(num):
            if num == 0:
                return 0
            return find_ones(num >> 1) + (num & 1)
            
        temp = nums[0]
        for i in range(1, len(nums)):
            temp = temp ^ nums[i]

        return find_ones(temp^k)