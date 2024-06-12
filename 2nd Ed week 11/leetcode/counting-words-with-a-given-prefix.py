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
            cur.count += 1

        cur.is_end = True

    def search(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return 0            
            cur = cur.children[char]
            
        return cur.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        return trie.search(pref)