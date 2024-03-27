class Solution:
    def isUgly(self, n: int) -> bool:
        def primes(num):
            divisor = 2
            factors = []
            
            while divisor * divisor <= num:
                while num % divisor == 0:
                    factors.append(divisor)
                    num //= divisor
                divisor += 1
            
            if num > 1:
                factors.append(num)
            return set(factors)
        
        if n <= 0: return False
        if n < 3: return True

        temp = list(primes(n))
        check = {2, 3, 5}
        
        for t in temp:
            if t not in check:
                return False
        
        return True