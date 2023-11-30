class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        answer = ""
        for i in range(0 , len(command)):
            if command[i] == "G":
                answer += "G"
            elif command[i] == "(":
                if command[i+1] == ")":
                    answer += "o"
                else:
                    answer += "al"
                    i += 2
            elif command[0] == "a":
                answer += "al"
        return answer