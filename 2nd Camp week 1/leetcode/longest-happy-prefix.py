class Solution:
    def longestPrefix(self, s: str) -> str:
        def KMP_preprocessing(p : str) -> list:
            m = len(p)    
            pi_table = [0] * m
            string = ''
            
            i, j = 0, 1
            while j < m:
                if p[i] == p[j]:
                    pi_table[j] = i + 1
                    i += 1
                    j += 1
                    # string = p[:i] if len(string) <= i+1 else string
                
                else:
                    if i == 0:
                        pi_table[j] = 0
                        j += 1
                    else:
                        i = pi_table[i-1]    
            
            string = p[:pi_table[-1]]
            
            return pi_table, string
        
        _, answer = KMP_preprocessing(s)
        return answer