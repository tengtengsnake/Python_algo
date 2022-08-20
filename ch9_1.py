
def bubble_sort(data):
    length=len(data)  #return 5
    for i in range(len(data)-1):  #有n筆資料需要排n-1次外層迴圈
        print("第%d次迴圈"%(i+1)) #i+1是因為迭代是從0開始
        for j in range(len(data)-1-i):
            if data[j]>data[j+1]:#左比右大,需要交換位置
                data[j],data[j+1]=data[j+1],data[j]  #位置交換
            print("第%d次內圈排序"%(j+1),data)
    return  data

data=[6,1,5,7,3]  # 建立數據
print("原始串列",data)
print("Bubble sort 排序結果",bubble_sort(data))





