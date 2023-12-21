class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Reverse the matrix or image
        n = len(image[0])
        for row in image:
            for i in range(n // 2):
                row[i], row[n - 1 - i] = row[n - 1 - i], row[i] 
        # change every 1 to 0 and vice versa
        for row in image:
            for i in range(n):
                if row[i] == 1:
                    row[i] = 0
                elif row[i] == 0:
                    row[i] = 1
        
        return image