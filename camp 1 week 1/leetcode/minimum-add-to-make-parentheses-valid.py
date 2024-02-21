class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened = 0
        closed = 0
        for char in s:
            if char == '(':
                opened += 1
            elif char == ')' and opened > 0:
                opened -= 1
            else:
                closed += 1
        
        return opened + closed