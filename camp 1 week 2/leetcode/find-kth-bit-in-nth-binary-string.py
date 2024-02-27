class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # def helper(n, k):
        #     if n == 1:
        #         return 0
        #     prev = helper(n - 1, ceil(k/2))
            
        #     if (prev == 0 and k % 2 == 0) or (prev == 1 and k % 2 != 0):
        #         return 1
        #     else:
        #         return 0
        def helper(n):
            if n == 1:
                return '0'
            prev = helper(n - 1)
            inverted = ''
            for char in prev:
                if char == '0':
                    inverted += '1'
                else:
                    inverted += '0'
            # inverted = inverted[::-1]

            curr = ''
            curr += prev + '1' + inverted[::-1]
            if n == 3:
                print(curr)
            return curr   
        answer = helper(n) 
        return answer[k - 1]
        