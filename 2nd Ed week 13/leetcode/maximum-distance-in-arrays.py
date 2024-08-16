class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_so_far = arrays[0][0]
        max_so_far = arrays[0][-1]
        answer = 0

        for i in range(1, len(arrays)):
            temp_max_diff = max((max_so_far - arrays[i][0]), (arrays[i][-1] - min_so_far))
            answer = max(answer, temp_max_diff)

            max_so_far = max(max_so_far, arrays[i][-1])
            min_so_far = min(min_so_far, arrays[i][0])
        
        return answer