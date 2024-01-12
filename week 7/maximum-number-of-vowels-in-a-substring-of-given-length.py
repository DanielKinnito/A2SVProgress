class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_dict = {'a', 'e', 'i', 'o', 'u'}

        left, right = 0, k - 1
        check_string = s[left:right + 1]
        count = sum(1 for char in check_string if char in vowel_dict)
        
        check = count

        while left < len(s) - k:
            if s[left] in vowel_dict:
                check -= 1
            
            left += 1
            right += 1

            if right < len(s) and s[right] in vowel_dict:
                check += 1
            
            count = max(count, check)
        
        return count