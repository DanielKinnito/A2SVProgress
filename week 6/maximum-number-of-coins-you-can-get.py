class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # answer = 0

        # for i in range(1, len(piles), 3):
        #     local = sorted(piles[i - 1: i + 2])
        #     answer += local[1]

        # return answer

        piles.sort()
        answer = 0

        for i in range(len(piles) // 3, len(piles), 2):
            answer += piles[i]

        return answer