class Node():
    def __init__(self,data=None):
        self.data=data
        self.next=None
class Linked_list():
    def __init__(self):
        self.head=None
    def print_linked_list(self):
        ptr=self.head
        while ptr:
            print(ptr.data)
            ptr=ptr.next
    def between(self,pre_node,newdata):
        '''在串列之間加入新節點'''
        if pre_node==None:
            print("缺插入節點的前一個節點")
            return 
        new_node=Node(newdata)#建立一個新節點
        new_node.next=pre_node.next
        pre_node.next=new_node
link=Linked_list()
link.head=Node(5)
n2=Node(15)
n3=Node(25)
link.head.next=n2
n2.next=n3
link.print_linked_list()
print("new linked_list")
link.between(n2,100)
link.print_linked_list()
