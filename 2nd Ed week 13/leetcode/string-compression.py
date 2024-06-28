class Solution:
    def compress(self, chars: List[str]) -> int:
        answer = 0
        i = 0

        while i < len(chars):
            letter = chars[i]
            count = 0
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1
            chars[answer] = letter
            answer += 1
            if count > 1:
                for c in str(count):
                    chars[answer] = c
                    answer += 1

        return answer