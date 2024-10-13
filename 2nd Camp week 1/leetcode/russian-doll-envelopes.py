class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        answer = 0
        dp = [0] * len(envelopes)

        for _, h in envelopes:
            left = 0
            right = answer
            
            while left < right:
                mid = (left + right) // 2
                
                if dp[mid] >= h:
                    right = mid
                else:
                    left = mid + 1
            
            dp[left] = h
            
            if left == answer:
                answer += 1

        return answer