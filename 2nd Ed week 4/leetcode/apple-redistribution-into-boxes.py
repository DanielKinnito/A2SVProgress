class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        all_apples = sum(apple)
        capacity.sort(reverse = True)

        for i in range(len(capacity)):
            all_apples -= capacity[i]
            if all_apples <= 0:
                return i + 1
        
        return len(capacity)