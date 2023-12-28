class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_coord = []

        for point in points:
            x_coord.append(point[0])
        
        max_area = 0
        x_coord.sort()

        for i in range(1, len(x_coord)):
            max_area = max(max_area, x_coord[i] - x_coord[i - 1])
        
        return max_area