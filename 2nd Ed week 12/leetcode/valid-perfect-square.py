class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num % sqrt(num) == 0