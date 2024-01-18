class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        max_freq = 0
        freq = {}
        result = 0

        for right in range(n):
            
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])

            if (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result