class Solution:
    def smallestValue(self, n: int) -> int:
        def prime_sum(num):
            answer = 0
            for i in range(2, num + 1):
                while num % i == 0:
                    num //= i
                    answer += i
            
            return answer

        temp = prime_sum(n)
        
        while n != temp:
            n = temp
            temp = prime_sum(n)
        
        return n