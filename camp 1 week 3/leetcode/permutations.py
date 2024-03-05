class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path):
            if len(path) == len(nums):
                answer.append(path[:])
                return

            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()

        answer = []
        backtrack([])

        return answer



        