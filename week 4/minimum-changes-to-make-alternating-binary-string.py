class Solution:
    def minOperations(self, s: str) -> int:
        cost10 = sum(int(c) == i % 2 for i, c in enumerate(s))
        cost01 = len(s) - cost10
        
        return min(cost10, cost01)