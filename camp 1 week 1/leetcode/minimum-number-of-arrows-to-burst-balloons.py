class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        print(points)
        bound = points[0][1]
        count = 1

        for point in points:
            if point[0] > bound:
                count += 1
                bound = point[1]
        return count