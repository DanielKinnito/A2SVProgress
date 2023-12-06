class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total_time = 0

        for point in range(len(points) - 1):
            x1, y1 = points[point]
            x2, y2 = points[point + 1]

            horizontal = abs(x2 - x1)
            vertical = abs(y2 - y1)
            
            diagonal = min(horizontal, vertical)
            remaining = max(horizontal, vertical) - diagonal

           
            total_time += diagonal + remaining

        return total_time