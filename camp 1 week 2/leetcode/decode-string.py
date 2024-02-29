class Solution:
    def decodeString(self, s: str) -> str:
        def helper(index):
            result = ""
            count = 0

            while index < len(s):
                if s[index].isdigit():
                    count = count * 10 + int(s[index])
                    index += 1
                elif s[index] == '[':
                    decoded, index = helper(index + 1)
                    result += count * decoded
                    count = 0
                elif s[index] == ']':
                    return result, index + 1
                else:
                    result += s[index]
                    index += 1

            return result, index

        return helper(0)[0]