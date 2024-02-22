class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map: # check against map.get()
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else: # add to stack if it is an opening bracket
                stack.append(char)
    
        return not stack # true if it is empty i.e. everything matched