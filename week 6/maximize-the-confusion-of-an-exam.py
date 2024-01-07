class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        max_consecutive = 0

        count_t = count_f = 0
        left = right = 0

        while right < n:
            if answerKey[right] == 'T':
                count_t += 1
            else:
                count_f += 1

            while min(count_t, count_f) > k:
                if answerKey[left] == 'T':
                    count_t -= 1
                else:
                    count_f -= 1
                left += 1

            max_consecutive = max(max_consecutive, right - left + 1)

            right += 1

        return max_consecutive