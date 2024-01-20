class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def dfs(current, visited, direction):
            if visited[current] == 2:
                return False

            if visited[current] == 1:
                return direction == (nums[current] > 0)

            visited[current] = 1
            next_index = (current + nums[current]) % n
            if next_index == current or nums[next_index] * nums[current] < 0:
                visited[current] = 2
                return False

            if dfs(next_index, visited, direction):
                visited[current] = 2
                return True

            visited[current] = 2
            return False

        for i in range(n):
            if nums[i] == 0:
                continue

            if dfs(i, [0] * n, nums[i] > 0):
                return True

        return False