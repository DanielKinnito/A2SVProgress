class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_val = (1 << maximumBit) - 1
        n = len(nums)
        xor_all = 0
        answer = []
        
        for num in nums:
            xor_all ^= num
        
        for i in range(n):
            max_xor_value = xor_all ^ max_val
            answer.append(max_xor_value)
            xor_all ^= nums[n - 1 - i]
        
        return answer