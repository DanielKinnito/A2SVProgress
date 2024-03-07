t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    mp = {}
    total = 0
    mp[0] = 1
    
    summation = 0
    for i in range(n):
        num = int(s[i]) - 1
        summation += num
        
        total += mp.get(summation, 0)
        mp[summation] = mp.get(summation, 0) + 1
    
    print(total)