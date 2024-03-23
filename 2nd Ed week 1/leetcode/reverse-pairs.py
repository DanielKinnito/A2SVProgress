class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(left_half, right_half):
            left, right = 0, 0
            len_left, len_right = len(left_half), len(right_half)

            merged = []
            count = 0

            while left < len_left and right < len_right:
                if right_half[right] > left_half[left]:
                    temp_check = left_half[left] / 2
                    count += bisect_left(right_half, temp_check)

                    merged.append(left_half[left])
                    left += 1
                else:
                    merged.append(right_half[right])
                    right += 1

            while left < len_left:
                merged.append(left_half[left])
                temp_check = left_half[left] / 2
                count += bisect_left(right_half, temp_check)
                left += 1

            while right < len_right:
                merged.append(right_half[right])
                right += 1

            return merged, count

        def merge_sort(left, right, nums):
            if left == right:
                return [nums[left]], 0

            mid = left + (right - left) // 2
            left_half, count_left = merge_sort(left, mid, nums)
            right_half, count_right = merge_sort(mid + 1, right, nums)

            merged, count = merge(left_half, right_half)
            count += count_left + count_right
            return merged, count

        _, count = merge_sort(0, len(nums) - 1, nums)
        return count