class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        one = ""
        two = ""
        for word in word1:
            one += word
        for word in word2:
            two += word
        return one == two