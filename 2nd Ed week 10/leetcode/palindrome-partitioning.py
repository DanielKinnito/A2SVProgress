class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        path = []
        
        def isPalindrome(string, first, last):
            while first < last:
                if string[first] != string[last]:
                    return False
                first += 1
                last -= 1
            return True

        def dp(idx):
            if idx >= len(s):
                answer.append(path.copy())
                return
            
            for i in range(idx, len(s)):
                if isPalindrome(s, idx, i):
                    path.append(s[idx:i+1])
                    dp(i + 1)
                    path.pop()
        
        dp(0)
        return answer