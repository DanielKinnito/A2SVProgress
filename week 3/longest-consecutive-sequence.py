class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        1 - make a dict{} to store nums
        2 - depending on whether the next number is in our dict{}
            -set left and right pointers to keep track
            -update current length and answer
        3 - update boundaries
        4 - return answer
        """
        if not nums:  # Check if nums is empty
            return 0

        answer = 0
        nums_dict = {}

        for num in nums:
            if num not in nums_dict:  #2
                left = nums_dict.get(num - 1, 0) 
                right = nums_dict.get(num + 1, 0)

                current_length = left + right + 1
                answer = max(answer, current_length)

                nums_dict[num] = current_length #3
                nums_dict[num - left] = current_length
                nums_dict[num + right] = current_length

        return answer