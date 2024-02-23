class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        answer = [0]* length

        for i in range(length):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                popped = stack.pop()
                answer[popped] = i - popped
            stack.append(i)
        
        return answer