from sys import stdin

t = int(stdin.readline().strip())
for _ in range(t):
    s = stdin.readline().strip()
    nums = [int(i) for i in s]
    
    answer = 0
    idx = 0
    found = 0 
    while idx < len(nums):
        n = 0 
        while idx <len(nums) and nums[idx] == 0:
            idx += 1 
            n = 1 
        if idx < len(nums)  and n and not found and nums[idx] == 1:
            while idx < len(nums) and nums[idx] == 1:
                idx += 1 
                found = 1
        j =  0 
        while idx < len(nums) and nums[idx] == 1:
            idx += 1 
            j  = 1
        answer += (j + n)
    print(answer)  
