from sys import stdin

t = int(stdin.readline().strip())
for _ in range(t):
    x, y = map(int, stdin.readline().strip().split())
    print(min(x, y), max(x, y))
