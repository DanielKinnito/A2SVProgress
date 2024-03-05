class Solution:
    @cache
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 3:
            return False
        return n % 3 == 0 and self.isPowerOfThree(n/3)