class Solution:
    def sortSentence(self, s: str) -> str:
        """
        1- cast the string to a list
        2- make an answer array of the same length
        3- for every word take its last character(usually a number) and store the rest in the answer array at position described by the last char -1.
        4- join the elements of the list with a space and return
        """
        words = s.split()
        n = len(words)
        answer = [""] * n

        for word in words:
            index = int(word[-1]) - 1
            answer[index] = word[:-1]

        return " ".join(answer)