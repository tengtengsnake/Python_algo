
class Node():
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Linked_list():
    '''鏈結串列'''
    def __init__(self):
        self.head=None  #鏈結串列第一個節點
    def print_list(self):
        '''列印鏈結串列'''
        ptr=self.head
        while ptr:
            print(ptr.data)
            ptr=ptr.next
    def begining(self,newdata):
        '''在第一個節點前插入新節點'''
        new_Node=Node(newdata)  #建立新節點
        new_Node.next=self.head #新節點指標指向舊頭(第一個)節點
        self.head=new_Node      #更新鏈結串列的第一個節點為新節點
link=Linked_list()  #利用類別建立物件
link.head=Node(5)
n2=Node(15)
n3=Node(25)
link.head.next=n2
n2.next=n3
link.print_list()
print("new linked_list")
link.begining(100)  #插入新資料新節點
link.print_list()
