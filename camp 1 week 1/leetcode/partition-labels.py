class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
            create a map for the last indices
            iterate through every char in s
            update step parameter: max()
            append the right pointer if it is equal to step
        """
        char_set = set(s)
        last = {}

        for char in char_set:
            last[char] = s.rindex(char)
        # print(last)
        left = 0
        # right = 0
        step = last[s[0]]
        answer = []
        for right in range(len(s)):
            step = max(step, last[s[right]])
            if right == step:
                answer.append(right - left + 1)
                left = right + 1
                if left + 1 < len(s):
                    step = last[s[left]]
        return answer