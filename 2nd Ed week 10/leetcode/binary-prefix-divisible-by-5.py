class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        binary = ''
        for num in nums:
            binary += str(num)
            if int(binary, 2) % 5:
                answer.append(False)
            else:
                answer.append(True)
        
        return answer