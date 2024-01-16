class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 1)
        order = [0] * len(s)

        for left, right, direction in shifts:
            diff = 1 if direction else -1
            
            prefix[left] += diff
            prefix[right + 1] -= diff

        total_shift = 0
        result = []

        for i in range(len(s)):
            total_shift += prefix[i]
            order[i] = (ord(s[i]) - ord('a') + total_shift) % 26
            result.append(chr(order[i] + ord('a')))

        return ''.join(result)