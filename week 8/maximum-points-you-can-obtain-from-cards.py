class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_pts = sum(cardPoints)
        window_size = len(cardPoints) - k

        current_sum = sum(cardPoints[:window_size])
        min_sum = current_sum

        for i in range(window_size, len(cardPoints)):
            current_sum += cardPoints[i] - cardPoints[i - window_size]
            min_sum = min(min_sum, current_sum)

        return total_pts - min_sum