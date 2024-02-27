class Solution:
    @cache
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(n, k):
            if n == 1:
                return 0
            prev = helper(n - 1, ceil(k/2))
            
            if (prev == 0 and k % 2 == 0) or (prev == 1 and k % 2 != 0):
                return 1
            else:
                return 0
        
        return helper(n,k)