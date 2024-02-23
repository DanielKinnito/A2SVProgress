class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        length = len(nums)

        for num in nums:
            if not stack or num < stack[-1][0]:
                stack.append((num, num))
            else:
                minimum = stack[-1][0] # 1 in 132
                # Pop from our stack as long us we find a greater
                # element than the top of stack(second number)
                while stack and stack[-1][1] < num:
                    stack.pop()
                # If 132 is found
                if stack and num > stack[-1][0] and num < stack[-1][1]:
                    return True
                else:
                    stack.append((minimum, num))

        return False