class Solution:
    def monkeyMove(self, n: int) -> int:
        def power_of_two(n: int) -> int:
            if n == 0:
                return 1
            half = power_of_two(n // 2)
            half = (half * half) % MOD
            if n % 2 != 0:
                half = (half * 2) % MOD
            return half

        MOD = 10**9 + 7
        total_ways = power_of_two(n)
        collision_ways = (total_ways - 2) % MOD
        
        return collision_ways