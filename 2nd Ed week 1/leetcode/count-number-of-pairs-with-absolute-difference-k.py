class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        answer = 0

        for i in range(k + 1, 101):
            find = count[i] * count[i - k]
            answer += find
        
        return answer