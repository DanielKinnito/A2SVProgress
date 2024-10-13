class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)

        answer = [0] * len(spells)
        
        for i, spell in enumerate(spells):
            index = bisect_left(potions, success / spell)
            answer[i] = m - index
        
        return answer