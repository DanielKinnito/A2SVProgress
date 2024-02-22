class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        i = 0
        while i < len(path):
            while i < len(path) and path[i] == '/':
                i += 1
            
            temp = ''
            while i < len(path) and path[i] != '/':
                temp += path[i]
                i += 1

            if temp == '.':
                continue
            elif temp == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(temp)
        print(stack)
        answer = '/' + '/'.join(stack)
        answer = answer[:-1] if len(answer) > 1 and answer[-1] == '/' else answer

        return answer if answer else '/'