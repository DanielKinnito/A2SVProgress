class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse = True)
        buckets = [0] * k
        self.unfairness = float('inf')

        def backtrack(index, buckets):
            if index >= len(cookies):
                self.unfairness = min(self.unfairness, max(buckets))
                return
            
            for i in range(k):
                if buckets[i] + cookies[index] >= self.unfairness or (i > 0 and buckets[i] == buckets[i - 1]):
                    continue

                buckets[i] += cookies[index]
                backtrack(index + 1, buckets)
                buckets[i] -= cookies[index]
        
        backtrack(0, buckets)
        
        return self.unfairness