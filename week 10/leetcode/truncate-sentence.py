class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split(' ')
        temp = words[:k]
        answer = ' '.join(temp)
        return answer