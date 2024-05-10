from sys import stdin
from collections import Counter

t = int(stdin.readline().strip())
for _ in range(t):
    s = stdin.readline().strip()
    temp = list(s)
    
    for i in range(1, len(temp)):
        if temp[i] != temp[i - 1]:
            temp[i], temp[i - 1] = temp[i - 1], temp[i]
            break
    answer = ''.join(temp)
    if answer != s:
        print('YES')
        print(answer)
    else:
        print('NO')
