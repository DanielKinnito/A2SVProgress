class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        stack = []
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        for idx, char in enumerate(s):
            if char not in seen:
                while stack and char < stack[-1] and idx < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
                seen.add(char)
                stack.append(char)
                    
        return ''.join(stack)