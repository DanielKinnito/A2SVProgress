class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        first, second = 0, 0
        len_s, len_t = len(s), len(t)

        while first < len_s and second < len_t:
            if s[first] == t[second]:
                second += 1
            first += 1

        return len_t - second