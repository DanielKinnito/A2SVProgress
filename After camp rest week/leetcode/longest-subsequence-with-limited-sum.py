class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        def helper(query):
            summ = 0
            for i, num in enumerate(nums):
                summ += num
                if summ > query:
                    return i
            return len(nums)

        return [helper(query) for query in queries]