class RecentCounter:

    def __init__(self):
        self.recent_requests = deque()

    def ping(self, t: int) -> int:
        self.recent_requests.append(t)

        while self.recent_requests[0] < t - 3000:
            self.recent_requests.popleft()
        
        return len(self.recent_requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)