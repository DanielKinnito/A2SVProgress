class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        que = deque(['0000'])
        seen = set(deadends)

        if target in seen or '0000' in seen:
            return -1
        if target == '0000':
            return 0
        
        answer = 0
        while que:
            answer += 1

            size = len(que)
            for _ in range(size):
                word = que.popleft()
                for i in range(4):
                    temp = word[i]
                    for delta in (1, -1):
                        new_digit = str((int(temp) + delta) % 10)
                        new_word = word[:i] + new_digit + word[i + 1:]
                        if new_word == target:
                            return answer
                        if new_word not in seen:
                            seen.add(new_word)
                            que.append(new_word)
                    word = word[:i] + temp + word[i + 1:]

        return -1