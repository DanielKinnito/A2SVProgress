class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dp(idx, jdx):
            if idx >= n or jdx >= m:
                return 0
                                    
            if (idx, jdx) not in memo:
                if text1[idx] == text2[jdx]:
                    memo[(idx, jdx)] = 1 + dp(idx + 1, jdx + 1)
                else:
                    take = dp(idx + 1, jdx)
                    nottake = dp(idx, jdx + 1)
                    memo[(idx, jdx)] = max(take, nottake)

            return memo[(idx, jdx)]
        memo = {}
        n = len(text1)
        m = len(text2)
                
        return dp(0, 0)