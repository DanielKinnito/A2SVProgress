class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        
        while left <= right:
            middle = (left + right) // 2
            squared = middle * middle

            if squared == x:
                return middle
            elif squared < x:
                left = middle + 1
            else:
                right = middle - 1
        
        return right