class CQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def appendTail(self, value: int) -> None:
        self.st1.append(value)

    def deleteHead(self) -> int:
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())

        return self.st2.pop() if self.st2 else -1


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
