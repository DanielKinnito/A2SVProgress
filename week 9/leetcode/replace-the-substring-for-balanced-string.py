class Solution:
    def isbalanced(self, m: dict, target: int) -> bool:
        for char in m:
            if m[char] > target:
                return False
        return True

    def balancedString(self, s: str) -> int:
        char_map = {"Q": 0, "W": 0, "E": 0, "R": 0}
        for char in s:
            char_map[char] += 1
        length = len(s)
        min_len = length
        target = length//4
        if self.isbalanced(char_map, target):
            return 0

        left = 0 
        right = 0
        while right < length:
            char_map[s[right]] -= 1
            if self.isbalanced(char_map, target):
                min_len = min(min_len, right - left + 1)
                
                while left <= right:
                    char_map[s[left]] += 1
                    left += 1
                    if self.isbalanced(char_map, target):
                        min_len = min(min_len, right - left + 1)
                    else:
                        break
            right += 1
        
        return min_len