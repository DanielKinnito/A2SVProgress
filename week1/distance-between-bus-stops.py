class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        total = sum(distance)
        if start > destination:
            start, destination = destination, start
        right_sum = 0
        for i in range(start, destination):
            right_sum += distance[i % len(distance)]
        if start > destination:
            right_sum = total - right_sum
        return min(right_sum, total - right_sum)