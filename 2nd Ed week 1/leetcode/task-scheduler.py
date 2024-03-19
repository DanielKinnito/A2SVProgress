class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        
        max_freq = max(count.values())
        max_occupy = (max_freq - 1) * (n + 1)

        n_max_freq = sum(value == max_freq for value in count.values())
        
        return max(max_occupy + n_max_freq, len(tasks))