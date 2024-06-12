class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        length = len(searchWord)
        sentence = list(sentence.split(' '))
        
        for i, word in enumerate(sentence):
            if word[:length] == searchWord:
                return i + 1
        
        return -1