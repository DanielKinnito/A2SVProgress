class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = [0]

        for char in s:
            
            if char == '(':
                stack.append(0)
            else:
                last_score = stack.pop()
                current_score = stack.pop()
                stack.append(current_score + max(2 * last_score, 1))

        return stack[0]