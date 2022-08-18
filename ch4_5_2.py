from queue import Queue
q=Queue() #建立物件
list=['漢堡','薯條','可樂']
for item in list:
    q.put(item)
    print('成功插入',item,'至queue')
print("queue output:")
while True:
    print(q.get())
