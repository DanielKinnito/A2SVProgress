class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        memo = {}

        def dp(i, j):
            if i >= n or j >= m:
                return float('inf')
            if i == n - 1 and j == m - 1:
                return max(1, 1 - dungeon[i][j])

            if (i, j) not in memo:
                right = dp(i, j + 1)
                down = dp(i + 1, j)
                min_health_needed = min(right, down) - dungeon[i][j]
                memo[(i, j)] = max(1, min_health_needed)

            return memo[(i, j)]

        return dp(0, 0)