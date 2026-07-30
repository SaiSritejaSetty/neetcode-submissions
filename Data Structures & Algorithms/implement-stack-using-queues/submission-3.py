class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        last = self.q[-1]
        for x in range(len(self.q)-1):
            self.q.append(self.q[x])
            self.q.pop()
        self.q.pop()
        return last
        
    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        lenght = len(self.q)
        if lenght > 0:
            return False
        if lenght == 0:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()