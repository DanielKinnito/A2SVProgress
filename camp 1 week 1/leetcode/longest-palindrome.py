class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_map = {}
        for char in s:
            char_map[char] = char_map.get(char, 0) + 1
            
        count = 0
        odd = 0
        for char in char_map:
            if char_map.get(char) % 2 == 0:
                count += char_map.get(char)
            else:
                odd += 1
                count += char_map.get(char) - 1
        
        return count + 1 if odd > 0 else count