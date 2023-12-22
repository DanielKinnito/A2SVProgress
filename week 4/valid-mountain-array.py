class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)

        if n < 3:
            return False

        mount_index = arr.index(max(arr))

        # The mount index must not be at the end
        if mount_index == 0 or mount_index == n - 1:
            return False

        # Check the first half
        for i in range(mount_index):
            if arr[i] >= arr[i + 1]:
                return False

        # Check the second half
        for i in range(mount_index, n - 1):
            if arr[i] <= arr[i + 1]:
                return False

        return True