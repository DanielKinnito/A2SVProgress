class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        temp = 0
        
        for num in nums:
            temp = (2 * temp + num) % 5
            answer.append(temp == 0)
        
        return answer