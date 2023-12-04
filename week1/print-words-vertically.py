class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        words = s.split()
        max_len = max(len(word) for word in words)
        result = []
        for i in range(max_len):
            down = ""
            for word in words:
                if i < len(word):
                    down += word[i]
                else:
                    down += " "
            result.append(down.rstrip(" ")) 
        return result