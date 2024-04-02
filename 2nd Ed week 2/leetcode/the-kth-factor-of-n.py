class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        divisor = 1
        
        while divisor * divisor <= n:
            if n % divisor == 0:
                factors.append(divisor)
                if n // divisor != divisor:
                    factors.append(n // divisor)
            divisor += 1
        
        factors.sort()
        return factors[k - 1] if k <= len(factors) else -1