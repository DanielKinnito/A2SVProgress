class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        answer = ""

        for i in range(0, len(s), 2 * k):
            temp = s[i:i + k]
            temp = temp[::-1]
            
            answer += temp + s[i + k:i + 2 * k]

        return answer