class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            num_str = [n for n in str(num)]
            num_str.sort()

            if num_str[0] == "0":
                # Find the first non-zero element and swap it with the leading '0'
                i = 1
                while i < len(num_str) and num_str[i] == "0":
                    i += 1

                if i < len(num_str):
                    num_str[0], num_str[i] = num_str[i], num_str[0]

            answer = ''.join(num_str)
            return int(answer)
    
        else:
            num = -1 * num
            nums = [n for n in str(num)]
            nums.sort(reverse=True)

            answer = ''.join(nums)

            return -1 * int(answer)