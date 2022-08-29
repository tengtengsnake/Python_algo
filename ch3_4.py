class Node():
    def __init__(self,data=None):
        self.data=data
        self.next=None
class Linked_list():
    '''linked list'''
    def __init__(self):
        self.head=None #鏈結串列的第一個節點
    def print_list(self):
        ptr=self.head
        while ptr:
            print(ptr.data)
            ptr=ptr.next
    def begining(self,newdata):
        '''insert a new node on the first place of a linked list'''
        new_node=Node(newdata)
        new_node.next=self.head
        self.head=new_node
    def ending(self,newdata):
        '''insert a new node on the last place of linked list'''
        new_node=Node(newdata)
        if self.head==None: #linked list is empty
            self.head=new_node #新節點就是頭拉
            return 
        last_ptr=self.head  #先把最後節點指向最前的節點
        while last_ptr.next:  #如果還有下一個節點
            last_ptr=last_ptr.next #迭代到串列最後的位址
        last_ptr.next=new_node #新節點加入到最後迭代的節點的後面就變成最後的節點了
   
        
link=Linked_list()
link.head=Node(5)
n2=Node(15)
n3=Node(25)
link.head.next=n2
n2.next=n3
link.print_list()
print("new linked_list")
link.begining(100)
link.print_list()
print("another new. linked_list")
link.ending(120)
link.print_list()
