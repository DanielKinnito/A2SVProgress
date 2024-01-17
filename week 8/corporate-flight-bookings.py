class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * (n + 1)

        for first, last, seat in bookings:
            prefix[first] += seat
            if last < n:
                prefix[last + 1] -= seat

        for i in range(1, n + 1):
            prefix[i] += prefix[i - 1]

        return prefix[1:]