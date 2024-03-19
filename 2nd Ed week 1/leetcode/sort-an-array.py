class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_array, right_array):
            left, right = 0, 0
            merged = []

            left_len, right_len = len(left_array), len(right_array)
            
            while left < left_len and right < right_len:
                if left_array[left] < right_array[right]:
                    merged.append(left_array[left])
                    left += 1
                else:
                    merged.append(right_array[right])
                    right += 1
            
            merged.extend(left_array[left:])
            merged.extend(right_array[right:])

            return merged
        
        def merge_sort(left, right, array):
            if left == right:
                return [array[left]]
            
            middle = (left + right) // 2
            left_array = merge_sort(left, middle, array)
            right_array = merge_sort(middle + 1, right, array)

            return merge(left_array, right_array)
        idx = len(nums) - 1
        return merge_sort(0, idx, nums)