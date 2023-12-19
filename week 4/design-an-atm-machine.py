class ATM:

    def __init__(self):
        self.banknotes_count = [0, 0, 0, 0, 0]
        self.banknotes = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount):
        for i in range(5):
            self.banknotes_count[i] += banknotesCount[i]

    def withdraw(self, amount):
        result = [0, 0, 0, 0, 0]

        original_count = self.banknotes_count.copy()

        for i in range(4, -1, -1):
            result[i] = min(amount // self.banknotes[i], self.banknotes_count[i])
            amount -= result[i] * self.banknotes[i]

        if amount != 0:
            return [-1]

        for i in range(5):
            self.banknotes_count[i] -= result[i]

        return result


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)