class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start = 0
        end = int(sqrt(c))
        
        while start <= end:
            temp = start**2 + end**2
            
            if temp == c:
                return True
            elif temp > c:
                end -= 1
            elif temp < c:
                start += 1

        return False                                              