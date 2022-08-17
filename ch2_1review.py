#create the Node
class Node():
    #記得初始化函數
    def __init__(self,data=None):
        self.data=data
        self.next=None
#建立節點  利用類別
n1=Node(5)
n2=Node(15)
n3=Node(25)
n1.next=n2
n2.next=n3
ptr=n1 #指標節點

while ptr:
    print(ptr.data)
    ptr=ptr.next
