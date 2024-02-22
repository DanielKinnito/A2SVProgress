class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        check = {'+':1, '-':1, '*':1, '/':1}
        if len(tokens) < 3:
            return int(tokens[0])

        for token in tokens:
            if token not in check:
                stack.append(token)
            else:
                operand_one = int(stack.pop())
                operand_two = int(stack.pop())

                if token == '+':
                    result = operand_two + operand_one
                    stack.append(result)
                elif token == '-':
                    result = operand_two - operand_one
                    stack.append(result)
                elif token == '*':
                    result = operand_two * operand_one
                    stack.append(result)
                elif token == '/':
                    if operand_two * operand_one > 0:
                        result = floor(operand_two / operand_one)
                    else:
                        result = ceil(operand_two / operand_one)
                    stack.append(result)
        
        return stack.pop()