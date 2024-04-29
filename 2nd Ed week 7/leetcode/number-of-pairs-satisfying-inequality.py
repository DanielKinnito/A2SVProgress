class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        def merge_sort(arr, left, right, diff, result):
            if left >= right:
                return
            
            mid = (left + right) // 2
            merge_sort(arr, left, mid, diff, result)
            merge_sort(arr, mid + 1, right, diff, result)
            merge(arr, left, mid, right, diff, result)
        
        def merge(arr, left, mid, right, diff, result):
            low = mid + 1
            high = mid + 1
            
            i = left
            while i <= mid:
                while high <= right and arr[i] > arr[high] + diff:
                    high += 1
                result[0] += right - high + 1
                i += 1
            
            sorted_arr = []
            k = 0
            i = left
            j = mid + 1
            
            while i <= mid and j <= right:
                if arr[i] < arr[j]:
                    sorted_arr.append(arr[i])
                    i += 1
                else:
                    sorted_arr.append(arr[j])
                    j += 1
            
            while i <= mid:
                sorted_arr.append(arr[i])
                i += 1
            
            while j <= right:
                sorted_arr.append(arr[j])
                j += 1
            
            for idx in range(len(sorted_arr)):
                arr[left + idx] = sorted_arr[idx]
        
        arr = [nums1[i] - nums2[i] for i in range(len(nums1))]
        result = [0]
        
        merge_sort(arr, 0, len(arr) - 1, diff, result)
        
        return result[0]