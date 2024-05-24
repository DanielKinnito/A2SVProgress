class TrieNode:
    def __init__(self):
        self.children = [ None for _ in range(2) ]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, number):
        cur = self.root
        for i in range(32, -1, -1):
            bit = 1 if number & (1 << i) else 0

            if not cur.children[bit]:
                cur.children[bit] = TrieNode()
            cur = cur.children[bit]
    
    def search(self, number):
        result = 0
        cur = self.root
        for i in range(32, -1, -1):
            bit = 1 if number & (1 << i) else 0

            if cur.children[1- bit]:
                cur = cur.children[1-bit]
                result = result | (1 << i)
            else:
                cur = cur.children[bit]
        return result

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.insert(num)
        
        ans = 0
        for num in nums:
            ans = max(ans, trie.search(num))
        return ans