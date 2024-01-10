class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        len_s, len_p = len(s), len(p)

        if len_s < len_p:
            return result

        s_freq = {}
        p_freq = {}

        for char in p:
            p_freq[char] = p_freq.get(char, 0) + 1

        for char in s[:len_p]:
            s_freq[char] = s_freq.get(char, 0) + 1

        if s_freq == p_freq:
            result.append(0)

        for i in range(len_p, len_s):
            s_freq[s[i]] = s_freq.get(s[i], 0) + 1
            s_freq[s[i - len_p]] -= 1
            
            if s_freq[s[i - len_p]] == 0:
                del s_freq[s[i - len_p]]

            if s_freq == p_freq:
                result.append(i - len_p + 1)

        return result
        """
        result = []
        len_s, len_p = len(s), len(p)


        """