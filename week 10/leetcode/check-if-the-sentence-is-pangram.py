class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        char_dict ={}
        for char in sentence:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        return len(char_dict) == 26