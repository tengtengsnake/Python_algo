
class Stack():
    def __init__(self):
        self.mystack=[]  #use list to simulate the stack 
    def my_push(self,data):
        self.mystack.append(data)
    def my_pop(self):
        self.mystack.pop()
    def size(self):
        return len(self.mystack)
    def isEmpty(self):
        return self.mystack==[]
    def cls(self):
        '''delete all data in the stack'''
        while True:
            self.my_pop()
        
stack=Stack()
fruits=['Grape','Mango','Apple']
for fruit in fruits:
    stack.my_push(fruit)
    print("將%s水果推入堆疊"%fruit)
print("堆疊有%d種水果"%stack.size())
print("the code is end")
stack.cls()


#while not stack.isEmpty:
   # print(stack.pop())
