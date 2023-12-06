class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        answer_array = []

        for num in nums:
            if nums.count(num) > length/3:
                answer_array.append(num)

        #To remove duplicate elements in the array
        answer_array = list(set(answer_array))

        return answer_array