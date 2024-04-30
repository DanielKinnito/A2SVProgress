class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0] * (n + 1)

        for i in range(1, n + 1):
            answer[i] = answer[i >> 1] + (i & 1)
        
        return answer