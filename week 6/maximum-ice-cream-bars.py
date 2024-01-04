class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        count_array = [0] * (max_cost + 1)
        
        for cost in costs:
            count_array[cost] += 1

        coins_left = coins
        count = 0

        for i in range(max_cost + 1):
            while count_array[i] > 0 and coins_left >= i:
                coins_left -= i
                count += 1
                count_array[i] -= 1

        return count