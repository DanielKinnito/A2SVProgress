class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        output = []
        asc = sorted(nums)
        
        for i in range(len(asc)):
            if asc[i] == target:
                output.append(i)
        
        return output