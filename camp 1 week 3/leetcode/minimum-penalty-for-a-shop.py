class Solution:
    def bestClosingTime(self, customers: str) -> int:
        answer = 0
        temp_profit = 0
        max_profit = 0

        for i in range(len(customers)):
            if customers[i] == 'Y':
                temp_profit += 1
            else:
                temp_profit += -1
            
            if temp_profit > max_profit:
                max_profit = temp_profit
                answer = i + 1

        return answer