class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        check_array = list(zip(position, speed))
        check_array.sort(key = lambda x: x[0], reverse = True)
        length = len(position)
        
        for combination in check_array:
            if stack:
                time_left = (target - combination[0]) / combination[1]
                if time_left > stack[-1]:
                    stack.append(time_left)
            else:
                stack.append((target - combination[0]) / combination[1])
        return len(stack)