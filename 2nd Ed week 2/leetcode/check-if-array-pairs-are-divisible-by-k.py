class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        check = defaultdict(int)

        for num in arr:
            if num % k == 0:continue
            
            find = k - num % k
            if find in check:
                check[find] -= 1
            
                if check[find] == 0:
                    del check[find]
            else:
                check[num%k] += 1

        return len(check) == 0