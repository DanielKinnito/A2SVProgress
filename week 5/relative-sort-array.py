class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ## map for the postions of numbers
        position_map = {val: i for i, val in enumerate(arr2)}
        # to sort arr1 in the order of arr2
        def custom_sort(x):
            if x in position_map:
                return position_map[x]
            else:
                return 1001 + x  # To ensure that elements not in arr2 are placed at the end
        arr1.sort(key = custom_sort)
        
        return arr1