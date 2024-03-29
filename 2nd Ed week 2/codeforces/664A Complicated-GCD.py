def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_range(a, b):
    result = a
    
    for i in range(a + 1, b + 1):
        result = gcd(result, i)
        if result == 1:
            break
    
    return result

first, last = map(int, input().split())

answer = gcd_range(first, last)
print(answer)