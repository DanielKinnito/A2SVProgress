class Solution:
    def minimizedStringLength(self, s: str) -> int:
        """
        Turning a string or any type of list to a set will produce a set of distinct elements. Going from that we would only have to return the length of that set
        """
        return len(set(s))