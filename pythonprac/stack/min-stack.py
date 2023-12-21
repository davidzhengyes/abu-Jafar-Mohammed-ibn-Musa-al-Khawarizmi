#https://leetcode.com/problems/min-stack/description/

class MinStack:
    def __init__(self):
        self.stack=[]
        self.min=[]

    def push(self,val):
        self.stack.append(val)
        if self.min:
            self.min.append(min(val,self.min[-1]))
        else:
            self.min.append(val)

    def pop(self):
        self.stack.pop()
        self.min.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min[-1]