class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        is_palindrome = [[False] * n for _ in range(n)]
        
        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 2 or is_palindrome[start + 1][end - 1]):
                    is_palindrome[start][end] = True
        
        dp = [float('inf')] * n
        dp[0] = 0
        
        for end in range(1, n):
            if is_palindrome[0][end]:
                dp[end] = 0
            else:
                for start in range(end):
                    if is_palindrome[start + 1][end]:
                        dp[end] = min(dp[end], dp[start] + 1)
        
        return dp[-1]