class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def findNextSmaller(arr):
            length = len(arr)
            stack = []
            next_smaller = [length] * len(arr)

            for i in range(len(arr)):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack_top = stack.pop()
                    next_smaller[stack_top] = i
                
                stack.append(i)
    
            return next_smaller
        
        def findPrevSmaller(arr):
            length = len(arr)
            stack = []
            prev_smaller = [-1] * len(arr)

            for i in range(len(arr)):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack_top = stack.pop()
                
                if stack:
                    prev_smaller[i] = stack[-1]
                
                stack.append(i)
    
            return prev_smaller
        
        prev_small = findPrevSmaller(heights[:])
        next_small = findNextSmaller(heights[:])
        
        answer = float('-inf')
        for i in range(len(heights)):
            compared = (next_small[i] - prev_small[i] - 1) * heights[i]
            answer = max(answer, compared)
        
        return answer