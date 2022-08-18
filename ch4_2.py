class Queue():
    def __init__(self): #define the initializer 
        self.queue=[]
    def enqueue(self,data):
        self.queue.insert(0,data)
    def dequeue(self):
        if len(self.queue):
            return self.queue.pop()  #打出末端資料
        else:
            print("the queue is empty")
    def size(self):
        print("the len of the queue",len(q.queue))
#建立物件
q=Queue()
q.enqueue('Grape')
q.enqueue('Mango')
q.enqueue('Apple')
q.size()


#q.size()
print("read the queue",q.dequeue())
print('read the queue',q.dequeue())
print('read the queue',q.dequeue())
print('read the queue',q.dequeue())
q.size()
