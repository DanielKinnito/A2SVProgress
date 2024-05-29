class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            cur.count += 1
        cur.is_end = True

    def search(self, word):
        result = 0
        cur = self.root
        for char in word:
            cur = cur.children[char]
            result += cur.count
        return result
        
    # def startsWith(self, prefix: str) -> bool:
    #     cur = self.root
    #     for char in prefix:
    #         if char not in cur.children:
    #             return False
    #         cur = cur.children[char]
    #     return True 

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()

        for word in words:
            trie.insert(word)
        answer = []
        for word in words:
            answer.append(trie.search(word))
        
        return answer