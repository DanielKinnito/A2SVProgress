class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = sorted(heights)
        if temp == heights:
            return 0
            
        count = 0

        for i in range(len(heights)):
            if temp[i] != heights[i]:
                count += 1
        
        return count