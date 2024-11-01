class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 1
        answer = s[0]

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            
            if count < 3:
                answer += s[i]
        
        return answer