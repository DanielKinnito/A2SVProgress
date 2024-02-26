class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        even_counts=n/2 if n%2 ==0 else n//2+1
        odd_counts=n//2
        
        def power(x,n):
            return pow(x,n,MOD)
        return (power(5, even_counts)*power(4,odd_counts))%MOD