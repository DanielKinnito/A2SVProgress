class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hashmap = defaultdict(int)
        answer = 0
        
        for hour in hours:
            remainder = hour % 24
            complement = (24 - remainder) % 24
            if complement in hashmap:
                answer += hashmap[complement]
            
            hashmap[remainder] += 1
        
        return answer