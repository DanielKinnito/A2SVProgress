class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        answer = 1
        minQ = deque()
        maxQ = deque()

        l = 0
        for r in range(len(nums)):
            while minQ and minQ[-1] > nums[r]:
                minQ.pop()
            
            minQ.append(nums[r])
            while maxQ and maxQ[-1] < nums[r]:
                maxQ.pop()
            
            maxQ.append(nums[r])
            
            while maxQ[0] - minQ[0] > limit:
                if minQ[0] == nums[l]:
                    minQ.popleft()
                if maxQ[0] == nums[l]:
                    maxQ.popleft()
                l += 1
            
            answer = max(answer, r - l + 1)

        return answer