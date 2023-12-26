class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)

        for i in range(n):
            min_index = i
            for j in range(i, n):
                if heights[j] > heights[min_index]:
                    min_index = j

            names[i], names[min_index] = names[min_index], names[i]
            heights[i], heights[min_index] = heights[min_index], heights[i]

        return names