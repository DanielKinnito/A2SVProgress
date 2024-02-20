class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """ Sort based on difference and reverse it.
            add for the counts of a and b until they are n/2
           """
        answer = 0
        n = len(costs)

        costs.sort(key=lambda cost: abs(cost[0] - cost[1]), reverse=True)

        countA = 0
        countB = 0

        for cost in costs:
            if cost[0] < cost[1]:
                if countA < n // 2:
                    answer += cost[0]
                    countA += 1
                else:
                    answer += cost[1]
                    countB += 1
            else:
                if countB < n // 2:
                    answer += cost[1]
                    countB += 1
                else:
                    answer += cost[0]
                    countA += 1

        return answer