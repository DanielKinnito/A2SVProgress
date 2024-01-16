class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_map = {}
        max_fruits = 0
        left = 0

        for right in range(len(fruits)):
            fruit_map[fruits[right]] = fruit_map.get(fruits[right], 0) + 1

            while len(fruit_map) > 2:
                fruit_map[fruits[left]] -= 1
                
                if fruit_map[fruits[left]] == 0:
                    del fruit_map[fruits[left]]
                
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits