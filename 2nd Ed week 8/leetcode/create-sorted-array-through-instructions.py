class Item:
    def __init__(self, num, index):
        self.num = num
        self.index = index

class Solution:
    def createSortedArray(self, instructions):
        kMod = 10**9 + 7
        n = len(instructions)
        answer = 0
        items = []
        lesser = [0]*n
        greater = [0]*n

        for i in range(n):
            items.append(Item(instructions[i], i))

        self.mergeSort(items, 0, n - 1, lesser, greater)

        for i in range(n):
            answer += min(lesser[i], greater[i])
            answer %= kMod

        return answer

    def mergeSort(self, items, l, r, lesser, greater):
        if l >= r:
            return

        m = (l + r) // 2
        self.mergeSort(items, l, m, lesser, greater)
        self.mergeSort(items, m + 1, r, lesser, greater)
        self.merge(items, l, m, r, lesser, greater)

    def merge(self, items, l, m, r, lesser, greater):
        lo = l
        hi = l

        for i in range(m + 1, r + 1):
            while lo <= m and items[lo].num < items[i].num:
                lo += 1
            while hi <= m and items[hi].num <= items[i].num:
                hi += 1
            lesser[items[i].index] += lo - l
            greater[items[i].index] += m - hi + 1

        sorted = [None]*(r - l + 1)
        k = 0
        i = l
        j = m + 1

        while i <= m and j <= r:
            if items[i].num < items[j].num:
                sorted[k] = items[i]
                i += 1
            else:
                sorted[k] = items[j]
                j += 1
            k += 1

        while i <= m:
            sorted[k] = items[i]
            i += 1
            k += 1

        while j <= r:
            sorted[k] = items[j]
            j += 1
            k += 1

        for i in range(l, r + 1):
            items[i] = sorted[i - l]