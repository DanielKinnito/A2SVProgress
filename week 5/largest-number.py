class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_str = list(map(str, nums))
        n = len(num_str)

        for i in range(n):
            for j in range(n - 1, i, -1):
                # Compare two  based on their concatenated forms
                if num_str[j-1] + num_str[j] < num_str[j] + num_str[j-1]:
                    # Swap if the concatenation is in the wrong order
                    num_str[j-1], num_str[j] = num_str[j], num_str[j-1]

        result = ''.join(num_str).lstrip('0') or '0'
        return result
        
        
        # num_strings = [str(num) for num in nums]
        # num_strings.sort(reverse=True)
        
        # comp_str = num_strings[0]
        # answer = ''
        
        # for num in num_strings:
        #     if num[0] == comp_str[0]:
        #         i, length = 1, min(len(num), len(comp_str))
                
        #         while i < length:
        #             if num[i] > comp_str[i]:
        #                 answer += num
        #                 break
        #             elif num[i] < comp_str[i]:
        #                 answer += comp_str
        #                 break
        #             else:
        #                 i += 1
        #     else:
        #         answer += max(num, comp_str)
        
        # return answer
        

        # return ''.join(num_string)

        
        # num_s = []
        # for num in nums:
        #     for i in range(len(str(num))):
        #         num_s.append(int(num[i]))
        
        # num_s.sort(reverse = True)
        # answer = ""
        
        # for i in range(len(num_s)):
        #     answer += str(num_s[i])

        # return answer