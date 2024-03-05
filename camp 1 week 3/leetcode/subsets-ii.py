class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(first, path):
            if first > n:
                return
            answer.append(path[:])

            for i in range(first, n):
                if i != first and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        n = len(nums)
        answer = []
        backtrack(0, [])

        return answer