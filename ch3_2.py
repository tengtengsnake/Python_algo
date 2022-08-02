class Node():  #建立類別
    def __init__(self,data=None):
        self.data=data  #data
        self.next=None  #pointer
class Linked_list():
    def __init__(self):
        self.head=None
    def print_list(self):
        ''' 列印linked_list'''
        ptr=self.head
        while ptr:
            print(ptr.data)
            ptr=ptr.next

link=Linked_list()  #利用類別建立物件
#開始將節點串起來
link.head=Node(5)
n2=Node(15)  #建立節點(物件n2)n2
n3=Node(25)  #建立節點(物件n3)n3
link.head.next=n2
n2.next=n3
link.print_list()
