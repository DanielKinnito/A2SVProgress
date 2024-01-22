class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_freq_map = [0] * 128
        t_freq_map = [0] * 128
        
        for char in t:
            t_freq_map[ord(char)] += 1
        left, right = 0, 0

        min_len = float('inf')
        min_window = ""
        required_chars = len(t)
        formed_chars = 0
        
        while right < len(s):
            s_freq_map[ord(s[right])] += 1
            if t_freq_map[ord(s[right])] > 0 and s_freq_map[ord(s[right])] <= t_freq_map[ord(s[right])]:
                formed_chars += 1
            right += 1

            while formed_chars == required_chars and left <= right:
                if right - left < min_len:
                    min_len = right - left
                    min_window = s[left:right]

                s_freq_map[ord(s[left])] -= 1
                if t_freq_map[ord(s[left])] > 0 and s_freq_map[ord(s[left])] < t_freq_map[ord(s[left])]:
                    formed_chars -= 1
                left += 1

        return min_window