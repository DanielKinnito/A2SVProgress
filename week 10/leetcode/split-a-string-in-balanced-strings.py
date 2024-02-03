class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        left = 0
        right = 0
        lcount = 0
        rcount = 0
        while right < len(s):
            if s[right] == 'L':
                lcount += 1
            else:
                rcount += 1
            if lcount == rcount:
                count += 1
                if right + 1 < len(s):
                    left = right + 1
                    right = left
                lcount = 0
                rcount = 0
            else:
                right += 1
        return count