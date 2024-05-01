class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer, x = 0, 0
        
        for num in nums:
            answer = (num ^ answer) & ~x
            x = (num ^ x) & ~answer
        
        return answer