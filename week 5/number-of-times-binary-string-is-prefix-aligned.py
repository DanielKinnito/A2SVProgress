class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        max_flipped_index = 0 # max_flipped index encountered so far

        for i, flip in enumerate(flips, start=1):
            max_flipped_index = max(max_flipped_index, flip)
            
            if max_flipped_index == i: # it means that all the bits up to the current index are set to 1
                count += 1

        return count