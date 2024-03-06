class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        answer = float('-inf')
        def heat(index):
            left = 0
            right = len(heaters) - 1
            least = float('inf')

            while left <= right:
                middle = (left + right) // 2

                if houses[index] == heaters[middle]:
                    least = 0
                    return least
                elif houses[i] < heaters[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
                least = min(least, abs(heaters[middle] - houses[index]))
            
            if left >= len(heaters):
                left = len(heaters) - 1
            return min(least, abs(heaters[left] - houses[index]))

        for i in range(len(houses)):
            curr = float('inf')
            least = heat(i)

            answer = max(answer, least)

        return answer