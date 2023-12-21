class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        #n or nlogn
        # for left in range(len(nums)):
        #     count = 0
        #     temp_left = left
            
        #     for right in range(temp_left + 1, len(nums)):
        #         if nums[temp_left] < nums[right]:
        #             temp_left = right
        #             right = temp_left + 1
                    
        #             count += 1
                
        #         if count >= 2:
        #             return True
        # return False
        #####################
        # stack = [nums[0]]
        
        # ptr = len(stack) - 1

        # for num in nums:
        #     if num < stack[ptr]:
        #         stack[ptr] = num
            
        #     if num > stack[ptr]:
        #         stack.append(num)
        #         ptr += 1
        
        # return True if len(stack) >= 3 else False

        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False