class MinStack:

    def __init__(self): 
        self.st1=[]
        self.st2=[]
        

    def push(self, val: int) -> None:
        self.st1.append(val)
        self.st2.append(min(val,self.st2[-1] if len(self.st2)>0 else val))
        

    def pop(self) -> None:
        self.st2.pop()
        self.st1.pop()

    def top(self) -> int:
        return self.st1[-1]
        

    def getMin(self) -> int:
        return self.st2[-1]
        
