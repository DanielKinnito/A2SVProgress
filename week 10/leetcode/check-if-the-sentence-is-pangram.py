class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        char_set = set(sentence)
        return len(char_set) == 26