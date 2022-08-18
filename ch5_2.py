#自行建立stack 並執行相關操作,自訂append pop
class Stack():
    def __init__(self):
        self.mystack=[] #建立空串列,利用list實踐stack
    def my_push(self,data):
        self.mystack.append(data)
    def my_pop(self):
        self.mystack.pop()
    def size(self):
        print("the len of the stack",len(self.mystack))
stack=Stack() #建立物件
fruits=['Grape','Mango','Apple']
for fruit in fruits:
    stack.my_push(fruit)
    print('將%s水果推入堆疊'%fruit)
print('堆疊有%d種水果',len(stack.mystack))
print(stack.mystack)
