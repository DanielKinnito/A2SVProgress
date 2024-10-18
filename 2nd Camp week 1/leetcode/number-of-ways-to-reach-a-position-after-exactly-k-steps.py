class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        difference = abs(endPos - startPos)
        
        if difference > k or (k - difference) % 2 != 0:
            return 0
        
        right_moves = (k + difference) // 2
        
        return comb(k, right_moves) % MOD