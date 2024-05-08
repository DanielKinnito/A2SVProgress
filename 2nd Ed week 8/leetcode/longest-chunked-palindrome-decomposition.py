class Solution:
    def longestDecomposition(self, text: str) -> int:
        left, right = deque(), deque()
        first, last = 0, len(text) - 1

        count = 0

        while first < last:
            left.append(text[first])
            right.appendleft(text[last])

            if left == right:
                count += 2
                left = deque()
                right = deque()

            first += 1
            last -= 1
 
        if first == last or (len(left) != 0 and len(right) != 0):
            return count + 1
        elif left != right:
            return count + 1
        else:
            return count