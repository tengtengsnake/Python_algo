#relative module with python
#剛剛是自訂函數來enqueue/dequeue data,利用list模擬queue
#python 有內建的enqueue/dequeue function->put(data),get()
from queue import*
#利用Queue() 可以直接建立一個空的queue  queue=[]
q=Queue()
q.put('Grape')  #enqueue data 'grape'
q.put('Mango')  
q.put('Apple')
#print("the len of queue",len()
print(q.empty())
while not q.empty():   #while True    not False == True
    print(q.get())  #use loop to dequeue(read) the data  using get()
