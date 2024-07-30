class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i + 1]:
                temp_max, maximum = -inf, -inf
                
                for j in range(i+1, n):
                    if arr[j] < arr[i] and arr[j] > maximum:
                        maximum = arr[j]
                        temp_max = j
                
                arr[i], arr[temp_max] = arr[temp_max], arr[i]
                return arr

        return arr