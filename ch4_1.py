class Queue():
    '''queue'''
    def __init__(self):
        self.queue=[] #使用串列list模擬
    def enqueue(self,data):
        '''data insert in to the queue use insert()'''
        self.queue.insert(0,data)  #(address index,data)
    def size(self):
        '''return queue size'''
        return len(self.queue)
q=Queue() #利用Queue類別建立物件q
q.enqueue('Grape')
q.enqueue('Mango')
q.enqueue('Apple')
print("the len of Queue is:",q.size())
#利用Queue class 建立物件q,q可以使用class 的東西,有了初始化函數後,物件q就有了個空串列
#函數有self,是為了搞清楚是哪一個物件在使用類別中的函數
