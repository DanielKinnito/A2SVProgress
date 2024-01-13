class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_operations = k
        white_count = 0

        for i in range(k):
            if blocks[i] == 'W':
                white_count += 1

        left = 0
        for right in range(k - 1, n):
            min_operations = min(min_operations, white_count)

            if blocks[left] == 'W':
                white_count -= 1
            left += 1

            if right + 1 < n and blocks[right + 1] == 'W':
                white_count += 1

        return min_operations