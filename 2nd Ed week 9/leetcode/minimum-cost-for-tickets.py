class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def dp(idx):
            if idx >= n:
                return 0
            
            if idx in memo:
                return memo[idx]
            one_day = dp(idx + 1) + costs[0]
            
            j = idx
            while j < n and days[j] < days[idx] + 7:
                j += 1
            seven_day = dp(j) + costs[1]

            j = idx
            while j < n and days[j] < days[idx] + 30:
                j += 1
            thirty_day = dp(j) + costs[2]

            memo[idx] = min(one_day, seven_day, thirty_day)
            return memo[idx]
            
        n = len(days)
        memo = {}
        return dp(0)