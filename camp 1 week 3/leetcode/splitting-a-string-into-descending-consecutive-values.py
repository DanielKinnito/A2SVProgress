class Solution:
    # @cache
    def splitString(self, s: str) -> bool:
        current = []
        def helper(index):
            if index >= len(s):
                return len(current) >= 2

            for i in range(index, len(s)):
                temp = int(s[index : i + 1])
                if len(current) == 0 or temp == current[-1] - 1:
                    current.append(temp)
                    if helper(i + 1):
                        return True
                    current.pop()
            return False
        
        return helper(0)