class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        unique_xor = 0
        for num in nums:
            unique_xor ^= num
        
        temp = unique_xor & (-unique_xor)
        
        a, b = 0, 0
        for num in nums:
            if num & temp:
                a ^= num
            else:
                b ^= num
        
        return [a, b]