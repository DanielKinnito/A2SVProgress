class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        min_len = len(strs[0])
        
        for string in strs[1:]:
            min_len = min(min_len , len(string))
            i = 0
            while i < min_len and prefix[i] == string[i]:
                i += 1

            prefix = prefix[:i]
            min_len = i
        return prefix