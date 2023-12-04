class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = ""
        i = 0
        
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                c_code = int(s[i:i + 2])
                answer += chr(ord('a') + c_code - 1)
                i += 3
            else:
                c_code = int(s[i])
                answer += chr(ord('a') + c_code - 1)
                i += 1

        return answer