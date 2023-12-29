class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        n = len(words)
        answer = [""] * n

        for word in words:
            index = int(word[-1]) - 1
            answer[index] = word[:-1]

        return " ".join(answer)