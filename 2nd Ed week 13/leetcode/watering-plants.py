class Solution(object):
    def wateringPlants(self, plants, capacity):
        steps = -1
        remaining_water = capacity

        for i in range(len(plants)):
            if remaining_water >= plants[i]:
                remaining_water -= plants[i]
                steps += 1
            else:
                steps += (i * 2) + 1
                remaining_water = capacity
                remaining_water -= plants[i]

        return steps + 1