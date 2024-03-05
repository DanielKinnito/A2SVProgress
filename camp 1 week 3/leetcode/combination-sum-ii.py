class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        summ = 0

        n = len(candidates)
        answer = set()

        def backtrack(index, path):
            nonlocal summ, n
            
            if summ == target and tuple(path) not in answer:
                answer.add(tuple(path[:]))
                return
            if summ > target:
                return
            
            if index > n:
                return

            for i in range(index, n):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                summ += candidates[i]

                backtrack(i + 1, path)
                summ -= candidates[i]
                path.pop()
        
        backtrack(0, [])

        return list(answer)