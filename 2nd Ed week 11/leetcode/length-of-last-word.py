class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = list(s.split(' '))
        for i in range(len(s)-1, -1, -1):
            if len(s[i]) > 0:
                return len(s[i])