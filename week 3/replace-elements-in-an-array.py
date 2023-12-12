class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        """
        1- Store the value and index in nums on a dictionary
        2- for the operations in operations, compare the first number 
            with the dictionary and replace that number with the second
            - and delete the first instance from the dict{}
        """
        nums_dict = {value: index for index, value in enumerate(nums)}
        
        for operation in operations:
            if operation[0] in nums_dict:
                index_to_update = nums_dict[operation[0]]
                
                nums[index_to_update] = operation[1]
                nums_dict[operation[1]] = index_to_update
                
                del nums_dict[operation[0]]
        
        return nums
