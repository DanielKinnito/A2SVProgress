class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        bits = {c: 1 << i for i, c in enumerate(ascii_lowercase[:10])}
        bitmask = 0

        count = defaultdict(int)
        count[0] = 1

        for c in word:
            bitmask ^= bits[c]
            count[bitmask] += 1

        answer = 0
        for bitmask, temp_count in count.items():
            answer += temp_count * (temp_count - 1) // 2
            for i in range(10):
                bitmask2 = bitmask ^ (1 << i)
                if bitmask2 < bitmask:
                    answer += temp_count * count.get(bitmask2, 0)

        return answer