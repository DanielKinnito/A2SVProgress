class Solution:
    def trap(self, height: List[int]) -> int:
        """
            Note to self: Use a decreasing monotonic stack.
        """
        length = len(height)
        stack = []
        answer = 0

        for i in range(length):
            while stack and height[stack[-1]] <= height[i]:
                stack_top = stack.pop()
                
                if stack:
                    curr_height = min(height[stack[-1]], height[i]) - height[stack_top]
                    curr_width = i - (stack[-1] + 1)

                    answer += curr_height * curr_width

            stack.append(i)
        
        return answer