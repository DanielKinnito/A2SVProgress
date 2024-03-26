class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        
        primes = [True] * (n + 1)
        primes[0], primes[1] = False, False
        
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
                    
        answer = [i for i in range(2, n) if primes[i]]
        
        return len(answer)