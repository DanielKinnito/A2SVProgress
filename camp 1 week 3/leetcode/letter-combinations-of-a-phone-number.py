class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {   '1':[],
                    '2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']
        }
        
        def backtrack(index, path):
            if len(path) == len(digits):
                appended = ''
                for char in path:
                    appended += char
                answer.append(appended)
                return 
            if index >= n:
                return
            
            for i in range(index, n):
                for char in phone[digits[i]]:
                    path.append(char)
                    backtrack(i + 1, path)
                    path.pop()
        
        n = len(digits)
        answer = []
        if n == 0:
            return []
        backtrack(0, [])

        return answer