class Solution:
    def fib(self, n: int) -> int:
        if n < 2: return n

        prev = 1
        prev_prev = 0

        answer = 0

        for _ in range(n -1):
            answer = prev + prev_prev
            prev_prev = prev
            prev = answer
        
        return answer