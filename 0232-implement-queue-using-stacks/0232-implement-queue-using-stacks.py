class MyQueue:

    def __init__(self):
        self.item=[]
        

    def push(self, x: int) -> None:
        self.item.append(x)

    def pop(self) -> int:
        x=self.item.pop(0)
        # return self.item[-1]
        return x
    def peek(self) -> int:
        if self.item:
            return self.item[0]

    def empty(self) -> bool:
        if self.item==[]:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()