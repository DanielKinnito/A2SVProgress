class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        ans, sum_n = 0, 0
        
        while sum_n < target or (sum_n - target) % 2 != 0:
            ans += 1
            sum_n += ans
            
        return ans