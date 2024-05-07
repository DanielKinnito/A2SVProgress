class Solution:
    def maxProduct(self, words: List[str]) -> int:
        answer = 0
        n = len(words)

        for i in range(n):
            first = set(words[i])
            for j in range(i + 1, n):
                second = set(words[j])

                if (first & second):
                    continue
                answer = max(answer, (len(words[i]) * len(words[j])))
        
        return answer