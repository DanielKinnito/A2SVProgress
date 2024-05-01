class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = bin(int(a, 2) + int(b, 2))
        return answer[2:]