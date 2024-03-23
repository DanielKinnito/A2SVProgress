class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decoder = {' ': ' '}

        curr_char = 'a'

        for char in key:
            if char not in decoder:
                decoder[char] = curr_char
                curr_char = chr(ord(curr_char) + 1)

        return ''.join(decoder[c] for c in message)