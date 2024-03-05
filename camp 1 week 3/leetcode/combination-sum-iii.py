class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))
        def backtrack(index, path, total):
            if len(path) == k and total == n:
                answer.append(path[:])
                return 
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path, total + nums[i])
                path.pop()
        
        answer = []
        backtrack(0, [], 0)
        
        return answer