class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        in_block_comment = False
        current_line = []

        for s in source:
            i = 0
            while i < len(s):
                if s[i:i + 2] == '/*' and not in_block_comment:
                    in_block_comment = True
                    i += 1
                elif s[i:i + 2] == '*/' and in_block_comment:
                    in_block_comment = False
                    i += 1
                elif s[i:i + 2] == '//' and not in_block_comment:
                    break
                elif not in_block_comment:
                    current_line.append(s[i])
                i += 1

            if current_line and not in_block_comment:
                result.append("".join(current_line))
                current_line = []

        return result
                    

        # answer = [""]

        # flag = False

        # for line in source:
        #     for i in range(len(line) - 1):
        #         if flag == True and line[i] != "*" and line[i + 1] != "/":
        #             continue
        #         else:
        #             flag = False

        #         if line[i] == "/" and line[i + 1] == "/":
        #             #pass
        #             answer.append(line[: i + 1])
        #         #else:  append
        #         elif line[i] == "/" and line[i + 1] == "*":
        #             answer.append(line[: i + 1])
                    
        #             flag = True # To indicate that the multiline comment started
        #         else:
        #             answer.append(line)                 

        # return answer

        # result = ''
        # final = ''
        
        # for s in source:
        #     for i in range(len(s)):
        #         if s[i] == '*/':
        #             if '/*' in result:
        #                start = result.find('/*')
        #                end = result.find('*/')
        #                if start != -1 and end != -1 and start < end:
        #                    final = result[:start] + result[end+1:]

        #         result += s[i]

        #         if  s[i] == '//' and i < len(s):
        #             for s in source:
        #                 pass
        #         else:
        #             final += s[i]
                
        # return list(final)