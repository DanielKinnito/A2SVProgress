class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        occurrence_map = { char: i for i, char in enumerate(s)}
        stack = []

        for i in range(len(s)):
            if s[i] not in seen:
                while stack and s[i] < stack[-1] and i < occurrence_map[stack[-1]]:
                    seen.remove(stack.pop())
                stack.append(s[i])
                seen.add(s[i])
            
        return ''.join(stack)