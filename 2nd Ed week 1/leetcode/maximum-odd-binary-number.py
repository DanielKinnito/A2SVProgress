class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        zeros = len(s) - ones
        
        answer = ''
        for _ in range(ones - 1):
            answer += '1'
        answer += '0' * zeros
        if ones:
            answer += '1'
        return answer