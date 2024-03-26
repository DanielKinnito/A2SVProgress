def primes(num):
    divisor = 2
    factors = set()
    
    while divisor * divisor <= num:
        while num % divisor == 0:
            factors.add(divisor)
            num //= divisor
        
        divisor += 1
    
    if num > 1:
        factors.add(num)
        
    return len(factors)

n = int(input())

answer = 0
for num in range(2, n + 1):
    if primes(num) == 2:
        answer += 1

print(answer)