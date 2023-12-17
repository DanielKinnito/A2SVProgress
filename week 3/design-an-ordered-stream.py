class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        # Insert the value at the corresponding index in the stream
        self.stream[idKey - 1] = value  
        result = []

        # Check if the current pointer points to a non-empty slot
        while self.pointer < len(self.stream) and self.stream[self.pointer] is not None:
            # Append the value to the result
            result.append(self.stream[self.pointer])  
            self.pointer += 1

        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)