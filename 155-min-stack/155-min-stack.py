class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        #return val

    def top(self) -> int:
        if len(self.stack)==0:
            return None
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
        temp_stack = self.stack.copy() #copy list to temp
        min_val = float("inf")
        while temp_stack:
            #loop all 
            min_val = min(temp_stack[-1], min_val)
            temp_stack.pop()
        return min_val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()