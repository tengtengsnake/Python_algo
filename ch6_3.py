class Node():
    def __init__(self,data=None):
        self.data=data 
        self.left_pointer=None
        self.right_pointer=None

    def print_root(self):
        print(self.data)

root=Node(20)  #利用Node() class 建立物件 root 
root.print_root()   #使用Node class中的print_root() 印出根節點中的data 20
