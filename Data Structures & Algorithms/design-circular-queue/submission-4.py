class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.count = 0
        self.front = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.count >= self.k:
            return False
        else: 
            new = (self.front+self.count) % self.k
            self.queue[new] = value
            self.count+=1
            return True

        

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        else:
            self.front = (self.front + 1) % self.k
            self.count -= 1
            return True
        

    def Front(self) -> int:
        if self.count>0:
            return self.queue[self.front]
        return -1
        

    def Rear(self) -> int:
        if self.count>0:
            return self.queue[(self.count-1+self.front)%self.k]
        return -1
        

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if self.count == self.k:
            return True
        return False

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()