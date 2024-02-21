class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        half = n//2

        total = [(a, b, a-b) for a, b in costs]
        total.sort(key = lambda x: x[2])

        return sum(a for a, b, difference in total[:half]) + sum(b for a, b, difference in total[half:])