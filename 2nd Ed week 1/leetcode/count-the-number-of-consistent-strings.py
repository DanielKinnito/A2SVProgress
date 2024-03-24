class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = Counter(allowed)
        answer = 0

        for word in words:
            temp = True
            for char in word:
                if char not in count:
                    break
            else:
                answer += 1
        
        return answer