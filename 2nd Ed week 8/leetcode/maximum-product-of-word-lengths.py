class Solution:
    def maxProduct(self, words: List[str]) -> int:
        answer = 0
        n = len(words)
        
        def bit_mask(word):
            ret = 0
            for c in word:
                ret  = ret | 1 << (ord(c) - ord('a'))
            return ret

        compare = []
        for word in words:
            compare.append(bit_mask(word))

        for i in range(n):
            for j in range(i + 1, n):
                if (compare[i] & compare[j]) > 0:
                    continue
                answer = max(answer, (len(words[i]) * len(words[j])))
        
        return answer