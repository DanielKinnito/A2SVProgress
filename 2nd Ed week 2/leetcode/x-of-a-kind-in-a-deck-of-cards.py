class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        count = Counter(deck)

        answer_gcd = 0
        for _, value in count.items():
            answer_gcd = gcd(answer_gcd, value)
        
        return answer_gcd >= 2