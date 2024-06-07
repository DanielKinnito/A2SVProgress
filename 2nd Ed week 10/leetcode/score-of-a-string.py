class Solution:
    def scoreOfString(self, s: str) -> int:
        answer = 0
        for i in range(1, len(s)):
            answer += abs(ord(s[i]) - ord(s[i-1]))
        return answer