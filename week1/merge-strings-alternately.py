class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n , m = len(word1) , len(word2)
        iterate = min(n,m)*2
        merged = ""
        word1_count , word2_count = 0 , 0
        flag = True
        for i in range(iterate):
            if flag == True:
                if word1_count < len(word1):
                    merged += word1[word1_count]
                    flag = False
                    word1_count += 1
                flag = False
            elif flag == False:
                if word2_count < len(word2):
                    merged += word2[word2_count]
                    flag = False
                    word2_count += 1
                flag = True
        if n > m:
            merged += word1[word1_count:]
        elif m > n:
            merged += word2[word2_count:]
            
        return merged