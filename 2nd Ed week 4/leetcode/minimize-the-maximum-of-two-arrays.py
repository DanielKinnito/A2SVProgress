class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        divi_lcm = lcm(divisor1, divisor2)
        left = 0
        right = 2 ** 31 - 1

        def is_possible(mid):
            count_1 = mid - mid // divisor1
            count_2 = mid - mid // divisor2
            total_count = mid - mid // divi_lcm
            return count_1 >= uniqueCnt1 and count_2 >= uniqueCnt2 and total_count >= uniqueCnt1 + uniqueCnt2

        while left < right:
            middle = (left + right) // 2
            if is_possible(middle):
                right = middle
            else:
                left = middle + 1

        return left