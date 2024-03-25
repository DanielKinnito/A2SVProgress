class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge(left_unsorted, left_sorted, left_count, right_unsorted, right_sorted, right_count):
            unsorted_merged, count_merged = [], []

            for i in range(len(left_count)):
                temp = bisect_left(right_sorted, left_unsorted[i])
                count_merged.append(left_count[i] + temp)
            
            count_merged.extend(right_count)
            unsorted_merged.extend(left_unsorted)
            unsorted_merged.extend(right_unsorted)

            return unsorted_merged, sorted(unsorted_merged), count_merged
            
        def merge_sort(left, right, nums):
            if left == right:
                return [nums[left]], [nums[left]], [0]
            
            middle = (left + right) // 2

            left_unsorted, left_sorted, left_count = merge_sort(left, middle, nums)
            right_unsorted, right_sorted, right_count = merge_sort(middle + 1, right, nums)

            return merge(left_unsorted, left_sorted, left_count, right_unsorted, right_sorted, right_count)
        
        _, sorted_nums, answer = merge_sort(0, len(nums) - 1, nums)
        print(sorted_nums)
        return answer