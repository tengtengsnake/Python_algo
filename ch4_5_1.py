lass Queue():
    #自定queue中的enqueue dequeue 功能
    def __init__(self):
        self.queue=[]  #使用串列List模擬queue
    def enqueue(self,data):
        self.queue.insert(0,data)
        print('成功插入',data,'至queue')
    def dequeue(self):
        self.queue.pop() #打出末端資料
    def size(self):
        print("The len of queue is:",len(q.queue))
q=Queue() #利用類別建立物件q
q.enqueue('Grape')
q.enqueue('Mango')
q.enqueue('Apple')
q.size()
