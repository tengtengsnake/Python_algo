class Node():
    '''建立節點'''
    def __init__(self,data=None):
        self.data=data
        self.next=None
class Linked_list():
    def __init__(self):
        self.head=None #指向linked_list的第一個指標
    def print_list(self):
        ptr=self.head
        while ptr:
            print(ptr.data)
            ptr=ptr.next
    def ending(self,newdata):
        '''在linked_list 尾端插入新資料'''
        new_node=Node(newdata)#建立新節點
        if self.head==None: #if true 表示linked_list is empty
            self.head=new_node
            return 
        last_ptr=self.head
        while last_ptr.next:
            last_ptr=last_ptr.next
        last_ptr.next=new_node
    def rm_node(self,rmkey):
        '''移除linked_list指定節點'''
        ptr=self.head #暫時指標
        if ptr:
            if ptr.data==rmkey:
                self.head=ptr.next
                return 
        while ptr:
            if ptr.data==rmkey:
                break
            prev=ptr
            ptr=ptr.next
        if ptr==None:
            return
        prev.next=ptr.next
link=Linked_list()
link.ending(5)
link.ending(15)
link.ending(25)
link.print_list()
print('the new linked_list')
link.rm_node(15) #指定移除節點15
link.print_list()        
