class Solution:
    def canCross(self, stones: List[int]) -> bool:
        indices = {stone: i for i, stone in enumerate(stones)}
        
        def dp(idx, prev):
            if idx == stones[-1]:
                return True
            
            if idx not in indices:
                return False

            if (idx, prev) not in memo:
                minus = False
                if prev > 1:
                    minus = dp(idx + prev -1,prev - 1)
                plus = dp(idx + prev + 1, prev + 1)
                same = dp(idx + prev, prev)
                
                memo[(idx, prev)] = minus or plus or same
            
            return memo[(idx, prev)]
        
        memo = {}
        return dp(1, 1)