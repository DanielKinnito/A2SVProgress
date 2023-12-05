class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        answer = [0] * len(s)
        for i in range(len(s)):
            answer[indices[i]] = s[i]
        return "".join(answer)