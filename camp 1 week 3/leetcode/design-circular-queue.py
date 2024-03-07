class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.front = 0
        self.rear = -1
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.size < self.capacity:
            self.rear = (self.rear + 1) % self.capacity
            self.size += 1
            self.queue[self.rear] = value
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.size > 0:
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        if self.size > 0:
            return self.queue[self.front]
        else:
            return -1

    def Rear(self) -> int:
        if self.size > 0:
            return self.queue[self.rear]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.capacity == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()