class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(first, path):
            if sum(path) == target:
                answer.append(path[:])
                return 

            if first > n:
                return

            for i in range(first, n):
                path.append(candidates[i])
                if sum(path) > target:
                    path.pop()
                    continue
                backtrack(i, path)
                path.pop()
        
        n = len(candidates)
        answer = []
        backtrack(0, [])

        return answer