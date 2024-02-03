class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        d = {}
        for jewel in jewels:
            if jewel not in d:
                d[jewel] = 1
            else:
                d[jewel] += 1

        for stone in stones:
            if stone in d:
                count += 1
        return count