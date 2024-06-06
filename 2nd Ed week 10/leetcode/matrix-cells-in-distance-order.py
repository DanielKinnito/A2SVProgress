class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        grid = [[row, col] for row in range(rows) for col in range(cols)]
        grid.sort(key = lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        
        return grid