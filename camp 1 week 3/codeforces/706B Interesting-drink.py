import bisect
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
k = int(input())

for _ in range(k):
    query = int(input())
    print(bisect.bisect_right(nums, query))