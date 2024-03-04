class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first, path):
            if len(path) == k:
                answer.append(path[:])
                return 

            for num in range(first, n + 1):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()
        
        answer = []
        backtrack(1, [])

        return answer