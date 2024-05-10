class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = ['']

        for c in s:
            temp = []
            if c.isalpha():
                for i in answer:
                    temp.append(i + c.lower())
                    temp.append(i + c.upper())
            else:
                for i in answer:
                    temp.append(i + c)
            answer = temp
        
        return answer