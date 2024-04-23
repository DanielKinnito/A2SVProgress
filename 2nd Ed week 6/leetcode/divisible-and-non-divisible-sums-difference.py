class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        def div(n, m):
            last = n // m * m

            if last == 0:
                return 0
            first = m
            count = (last - first) // m + 1
            return (first + last) * count // 2
            
        summ = (1 + n) * n // 2
        num2 = div(n, m)
        num1 = summ - num2
        return num1 - num2