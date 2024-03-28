class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        primes = set()
        seive = [True] * (n + 1)
        
        for divisor in range(2, int(n**0.5) + 1):
            if seive[divisor]:
                for multiple in range(divisor * divisor, n + 1, divisor):
                    seive[multiple] = False
        
        answer = []
        for num in range(2, n // 2 + 1):
            if seive[num] and seive[n - num]:
                answer.append([num, n - num])
        
        return answer