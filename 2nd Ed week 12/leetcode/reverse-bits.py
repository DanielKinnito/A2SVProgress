class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        
        length = 32
        for i in range(length):
            if n & (1 << i):
                answer |= 1 << (31 - i)

        return answer