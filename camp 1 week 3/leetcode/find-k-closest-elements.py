class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort()
        temp = []

        for i, num in enumerate(arr):
            temp.append((num, abs(num - x)))
        
        temp.sort(key = lambda x: x[1])
        
        answer = [0] * len(temp)
        for i in range(len(temp)):
            answer[i] = temp[i][0]
        
        answer = answer[:k]
        answer.sort()
        
        return answer