class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def dp(i, j):
            if i < 0:
                return True
            if j < 0:
                return False
            
            if (i, j) not in memo:
                if s[i] == t[j]:
                    memo[(i, j)] = dp(i - 1, j - 1)
                else:
                    memo[(i, j)] = dp(i, j - 1)

            return memo[(i, j)]
        
        memo = {}
        return dp(len(s)- 1, len(t) - 1)