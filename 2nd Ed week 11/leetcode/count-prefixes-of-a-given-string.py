class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
        self.count = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end = True
        cur.count += 1

    def search(self, word):
        result = 0
        cur = self.root
        for char in word:
            if char not in cur.children:
                return result

            cur = cur.children[char]
            if cur.is_end: result += cur.count           
            
        return result

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        trie = Trie()

        for word in words:
            trie.insert(word)
        
        return trie.search(s)