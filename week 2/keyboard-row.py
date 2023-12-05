class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        answer = []

        for word in words:
            row = None
            for char in word.lower():
                if char in first:
                    current_row = first
                elif char in second:
                    current_row = second
                elif char in third:
                    current_row = third
                else:
                    break
                if row is None:
                    row = current_row
                elif row != current_row:
                    break
            else:
                answer.append(word)

        return answer