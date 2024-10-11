class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        sorted_freq = sorted(freq.values(), reverse=True)
        presses = 0

        for i, count in enumerate(sorted_freq):
            group = (i // 8) + 1
            presses += count * group

        return presses