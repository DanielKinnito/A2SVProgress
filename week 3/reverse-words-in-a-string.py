class Solution:
    def reverseWords(self, s: str) -> str:
        """
        1 - Split the words by space
        2 - Remove empty strings resulting from leading/trailing spaces
        3 - Reverse the list
        4 - Join the reversed list into a string with a single space between words
        """
        words = [word for word in s.split(" ") if word != ""]
        
        reversed_words = words[::-1]
        reversed_string = " ".join(reversed_words)
        
        return reversed_string