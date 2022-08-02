class Node():
    #節點
    def __init__(self,data=None):
        self.data=data
        self.next=None

n1=Node(5)   #呼叫method Node 並且傳入value 給初始化函數  n1 節點的值是5   "注意這邊n1是一個物件"
n2=Node(15)  #n2's value is 15
n3=Node(25)  #n3's value is 25

n1.next=n2   #n1指向下一個節點n2
n2.next=n3   #same as above
ptr=n1       #ptr 指向n1 節點
while ptr:
    print(ptr.data)  #列印節點
    ptr=ptr.next    #指標指向下一個節點
