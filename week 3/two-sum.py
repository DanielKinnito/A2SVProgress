class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1 - Make an empty dict{}
        2 - iterate through elements of nums and if the the other number is in the dictionary ( other  = target - original number)
        3 - return those numbers if found
        4 - append the number in the dictionary, to be compared for other iterations
        """
        nums_dict = {}#1
        
        for i in range(len(nums)): #2
            num_one = nums[i]
            num_two = target - num_one
            
            if num_two in nums_dict:# 3
                return [nums_dict[num_two], i]

            nums_dict[num_one] = i #4