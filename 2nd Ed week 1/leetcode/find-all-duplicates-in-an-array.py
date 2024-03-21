class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        count = Counter(nums)

        for key in list(count.keys()):
            if count[key] != 1:
                answer.append(key)
        
        return sorted(answer)