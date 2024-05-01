class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x, answer = 0, 0
        
        for num in nums:
            x = (num ^ x) & ~answer
            answer = (num ^ answer) & ~x
        
        return x