class Solution:

    def __init__(self, w: List[int]):
        self.prefix = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        return bisect_left(self.prefix, random.random() * self.prefix[-1])


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()