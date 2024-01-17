class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sorted_trips = sorted(trips, key=lambda x: x[2])

        length = sorted_trips[-1][2]
        prefix = [0] * (length + 1)

        for passengers, pick_up, drop_off in sorted_trips:
            prefix[pick_up] += passengers
            if drop_off < length:
                prefix[drop_off] -= passengers

        current_capacity = 0
        for num in prefix:
            current_capacity += num
            if current_capacity > capacity:
                return False

        return True