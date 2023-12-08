class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        words = []
        left = 0

        for space in spaces:
            words.append(s[left:space])
            left = space

        words.append(s[left:])
        answer = " ".join(words)
        
        return answer