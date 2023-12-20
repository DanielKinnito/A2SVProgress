class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = list(reversed(digits))
        carry = 1 

        for i in range(len(answer)):
            temp_sum = answer[i] + carry
            answer[i] = temp_sum % 10
            carry = temp_sum // 10

        if carry:
            answer.append(carry)

        return list(reversed(answer))