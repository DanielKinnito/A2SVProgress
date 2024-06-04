class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end = True

    def search(self, word):
        cur = self.root
        for char in word:
            if not cur.children[char]:
                return False
            if not cur.children[char].is_end:
                return False
            
            cur = cur.children[char]
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        words.sort()
        for word in words:
            trie.insert(word)
        answer = ''
        for word in words:
            if trie.search(word):
                if answer < word and len(word) > len(answer):
                    answer = word
        
        return answer