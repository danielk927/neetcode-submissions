class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        self.temp = []
        minTracker = self.stack[-1]
        self.stack.pop()
        self.temp.append(minTracker)
        while self.stack:
            teemp = self.stack[-1]
            minTracker = min(minTracker, teemp)
            self.temp.append(teemp)
            self.stack.pop()
        while self.temp:
            teeemp = self.temp[-1]
            self.temp.pop()
            self.stack.append(teeemp)
        return minTracker




            


