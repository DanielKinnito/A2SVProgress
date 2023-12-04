class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        alien_dict = {}
        for i in range(len(order)):
            alien_dict[order[i]] = i

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            for j in range(min(len(word1), len(word2))):
                char1, char2 = word1[j], word2[j]

                if alien_dict[char1] > alien_dict[char2]:
                    return False
                elif alien_dict[char1] < alien_dict[char2]:
                    break
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return False

        return True
