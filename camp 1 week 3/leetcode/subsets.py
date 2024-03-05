class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first, path):
            answer.append(path[:])
            if first > n + 1:
                # answer.append(path[:])
                return

            for i in range(first, n):
                path.append(nums[i])

                backtrack(i + 1, path)
                path.pop()
        
        n = len(nums)
        answer = []
        backtrack(0, [])

        return answer