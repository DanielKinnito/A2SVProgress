class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            index = ord(char) - 97
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
            cur.count += 1
        cur.is_end = True
    
    def search(self, word):
        cur = self.root
        prefix = ''
        for char in word:
            index = ord(char) - 97
            if not cur.children[index]:
                break
            cur = cur.children[index]
            prefix += char
            if cur.is_end:
                return prefix
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        answer = []
        sentence = list(map(str, sentence.split(' ')))
        for word in sentence:
            hold = trie.search(word)
            if len(hold) == 0:
                answer.append(word)
            else:
                answer.append(hold)
        return ' '.join(answer)