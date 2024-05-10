from sys import stdin
comp = [12, 11, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]

t = int(stdin.readline().strip())
for _ in range(t):
    a, b, c, d = map(int, stdin.readline().strip().split())
    
    min_one = min(a, b)
    max_one = max(a, b)
    
    min_two = min(c, d)
    max_two = max(c, d)
    
    if min_two < min_one < max_two and max_one > max_two:
        print('YES')
    elif min_one < min_two < max_one and max_two > max_one:
        print('YES')
    else:
        print('NO')
