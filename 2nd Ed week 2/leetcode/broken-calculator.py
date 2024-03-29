class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        answer = 0
        
        while target > startValue:
            if target % 2 == 0:
                target //= 2
            
            else:
                target += 1
            
            answer += 1
        
        answer += startValue - target
        return answer