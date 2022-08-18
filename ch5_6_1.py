class Stack():
    def __init__(self):
        self.mystack=[]  #use list to simulate the stack 
    def my_push(self,data):
        self.mystack.append(data)
    def my_pop(self):
        self.mystack.pop()
    def size(self):
        return len(self.mystack)
    def get(self):
        '''回傳stack 頂端值卻又不刪除'''
        result=self.mystack.pop()
        self.my_push(result)
        return result
    def isEmpty(self):
        return self.mystack==[]
    
stack=Stack()
fruits=['Grape','Mango','Apple']
for fruit in fruits:
    stack.my_push(fruit)
    print("將%s水果推入堆疊"%fruit)
print("堆疊有%d種水果"%stack.size())
get_top_value=stack.get()
print(get_top_value)
print(stack.mystack) 
print(stack.mystack) 
print(stack.mystack)  #經過確認apple 還在stack 中
