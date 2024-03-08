n = int(input())

positions = list(map(int, input().split()))
speeds = list(map(int, input().split()))

persons = {}
for i in range(n):
    if positions[i] not in persons:
        persons[positions[i]] = speeds[i]

sorted_positions = sorted(positions)

def condition(mid):
    upper = min(num + mid * persons[num] for num in sorted_positions)
    lower = max(num - mid * persons[num] for num in sorted_positions)
    return upper > lower

low = 0
high = max(sorted_positions)

while abs(high - low) > 10**-6:
    middle = (high + low) / 2
    if condition(middle):
        high = middle
    else:
        low = middle

print(low)