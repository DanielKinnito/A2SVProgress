class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:        
        answer = set()
        for num in nums:
            divisor = 2
            
            while divisor * divisor <= num:
                while num % divisor == 0:
                    answer.add(divisor)
                    num //= divisor
                
                divisor += 1
            
            if num > 1:
                answer.add(num)
        
        return len(answer)