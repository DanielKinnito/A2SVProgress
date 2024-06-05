class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        frequency = Counter(words[0])

        for word in words:
            frequency &= Counter(word)
        
        return list(frequency.elements())