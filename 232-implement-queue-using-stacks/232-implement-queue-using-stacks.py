class MyStack:
    def __init__(self):
        self.stack = []
        
    def push(self,x: int):
        try:
            self.stack.append(x)
        except:
            raise Exception("Error: stack is full") #unreachable code as no list len restriction
    
    def pop(self):
        try:
            print(self.stack[-1])
            return self.stack.pop()
        except:
            raise Exception("Error: stack is empty") 
        
    def peek(self):
        try:
            return self.stack[-1]
        except:
            raise Exception("Error: stack is empty")
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False
    
class MyQueue:
    def __init__(self):
        self.queue = MyStack()

    def push(self, x: int) -> None:
        try:
            self.queue.push(x)
            print(self.queue.stack)
        except:
            raise Exception("Error: Queue is Full")

    def pop(self) -> int:
        currStack = self.queue
        tempStack = MyStack()
        while not self.empty():
            pop_elem=currStack.pop()
            tempStack.push(pop_elem)
            print("pop elem", pop_elem)
        pop_elm = tempStack.pop()
        while not tempStack.isEmpty():
            currStack.push(tempStack.pop())
        return pop_elm

    def peek(self) -> int:
        currStack = self.queue
        tempStack = MyStack()
        while not self.empty():
            pop_elem=currStack.pop()
            tempStack.push(pop_elem)
            print("pop elem", pop_elem)
        peek_elm = tempStack.peek()
        while not tempStack.isEmpty():
            currStack.push(tempStack.pop())
        return peek_elm

    def empty(self) -> bool:
        return self.queue.isEmpty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()