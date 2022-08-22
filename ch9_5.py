def selection_sort(data):
    length=len(data)
    for i in range(length-1):
        index=i  #紀錄最小值索引
        for j in range(i+1,length):#前面一排序的就不用排ㄌ 
            if data[index]>data[j]: #如果前面大於後面
                index=j  #紀錄最小值索引
        if i==index:  #如果目前索引已經最小值索引
            pass #不更動
        else:
                data[i],data[index]=data[index],data[i]
    return data

data=[6,1,5,7,3]
print("原始串列",data)
print("排序結果",selection_sort(data))
