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
