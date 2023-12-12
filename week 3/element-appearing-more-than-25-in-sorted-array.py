class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        """
        1 - Return the value that has count() greater than length of arr 
        floor divided by 4
        """
        quarter = len(arr) // 4
        for num in arr:
            if arr.count(num) > quarter:
                return num