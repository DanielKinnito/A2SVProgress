class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        col_map = Counter(answers)
        result = 0
        for key in col_map:
            result += ceil( col_map[key] / (key + 1)) * (key + 1)
        return result