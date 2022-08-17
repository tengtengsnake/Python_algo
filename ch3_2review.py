#traverse the linked_list
class Node():
    '''node'''
    def __init__(self,data=None):
        self.data=data
        self.next=None
class Linked_list():
    '''linked_list'''
    def __init__(self):
        self.head=None
    def print_list(self):
        '''print out the linked_list'''
        ptr=self.head
        while ptr:
            print(ptr.data)
            ptr=ptr.next
link=Linked_list()  #建立物件link
link.head=Node(5)
n2=Node(15)
n3=Node(25)
link.head.next=n2
n2.next=n3
link.print_list()
