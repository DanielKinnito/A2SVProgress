class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        """
        1 - Create a set with unique numbers from both decks.
        2 - Iterate through the set to find the minimum number that is not present on both the front and back of any card.
        3 - Return the minimum number if found; otherwise, return 0.
        """
        card = set(fronts + backs)
        result = float('inf')

        for num in card:
            if num not in fronts or num not in backs:
                result = min(result, num)

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                card.discard(fronts[i])
                card.discard(backs[i])

        for num in card:
            return num

        return 0