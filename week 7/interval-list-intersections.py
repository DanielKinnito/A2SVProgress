class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer = []
        left, right = 0, 0

        while left < len(firstList) and right < len(secondList):
            low = max(firstList[left][0], secondList[right][0])
            high= min(firstList[left][1], secondList[right][1])
            if low <= high:
                answer.append([low, high])
            if firstList[left][1] < secondList[right][1]:
                left += 1
            else:
                right += 1

        return answer