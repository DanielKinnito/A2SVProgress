class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(1, len(arr) - 1):
            if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i - 1] % 2 != 0:
                return True
        
        return False