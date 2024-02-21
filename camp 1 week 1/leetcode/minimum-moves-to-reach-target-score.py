class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target > 1 and maxDoubles > 0:
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            count += 1
        return count + target - 1