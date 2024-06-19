class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        def helper(waitingDays):
            result = 0
            req_flowers = k
            for day in bloomDay:
                if day > waitingDays:
                    req_flowers = k
                else:
                    req_flowers -= 1
                    if req_flowers == 0:
                        result += 1
                        req_flowers = k
            return result

        left = min(bloomDay)
        right = max(bloomDay)

        while left < right:
            middle = (left + right) // 2
            if helper(middle) >= m:
                right = middle
            else:
                left = middle + 1

        return left