from sys import stdin

t = int(stdin.readline().strip())
for _ in range(t):
    x = int(stdin.readline().strip())
    
    answer = None
    flag = False
    zero = None
    for i in range(31):
        if x & (1<<i) > 0:
            if answer == None:
                answer = 1<<i
            else:
                flag = True
                break
        else:
            if zero == None: zero = i
    
    if not flag:
        answer = answer | (1 << zero)
        
    print(answer)