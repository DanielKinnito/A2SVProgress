class Bitset:

    def __init__(self, size: int):
        self.string = ["0"] * size
        self.reversed = ["1"] * size
        self.count_val = 0

    def fix(self, idx: int) -> None:
        if self.string[idx] == "0":
            self.count_val += 1
        self.string[idx] = "1"
        self.reversed[idx] = "0"

    def unfix(self, idx: int) -> None:
        if self.string[idx] == "1":
            self.count_val -= 1
        self.string[idx] = "0"
        self.reversed[idx] = "1"

    def flip(self) -> None:
        self.string, self.reversed = self.reversed, self.string
        self.count_val = len(self.string) - self.count_val

    def all(self) -> bool:
        return self.count_val == len(self.string)

    def one(self) -> bool:
        return bool(self.count_val)

    def count(self) -> int:
        return self.count_val

    def toString(self) -> str:
        return "".join(self.string)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()