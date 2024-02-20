class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        answer = 0
        while k > 0:
            if numOnes >= 1:
                k -= 1
                numOnes -= 1
                answer += 1
            elif numZeros >= 1:
                k -= 1
                numZeros -= 1
                answer = answer
            else:
                k -= 1
                numNegOnes -= 1
                answer -= 1
        
        return answer