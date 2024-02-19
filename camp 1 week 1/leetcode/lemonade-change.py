class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
                fives -= 1
            elif bill == 20:
                if tens >= 1:
                    tens -= 1
                    fives -= 1
                else:
                    fives -= 3
            if fives < 0 or tens < 0:
                return False
        return True