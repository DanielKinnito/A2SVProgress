class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        answer = 0

        for num in s:
            if num == '1':
                count += 1
            else:
                answer += count
        
        return answer