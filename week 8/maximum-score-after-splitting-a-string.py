class Solution:
    def maxScore(self, s: str) -> int:
        prefix = s[: 1].count('0')
        suffix = s[1: ].count('1')

        answer = prefix + suffix

        left = 1
        while left < len(s) - 1:
            if s[left] == '0':
                prefix += 1
            elif s[left] == '1':
                suffix -= 1
            
            temp = prefix + suffix
            answer = max(answer, temp)
            left += 1
        
        return answer
