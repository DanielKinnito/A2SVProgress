class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total, cur = 0, 0
        starting = 0

        for i in range(n):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]

            if cur < 0:
                starting = i + 1
                cur = 0
        
        if total < 0:
            return -1
        else:
            return starting