from curses.ascii import NL


def cocktail_sort(nLst):
    '''雞尾酒排序'''
    n=len(nLst)  #return n=5
    is_sorted=True #紀錄有分類完成或沒有
    start=0  #前端索引
    end=n-1  #末端索引
    while is_sorted: #執行就對拉
        is_sorted=False  #重置是否排序完成
        for i in range(start,end):  #0~4
            if(nLst[i]>nLst[i+1]): #如果左邊元素於右邊
                nLst[i],nLst[i+1]=nLst[i+1],nLst[i]
                is_sorted=True #排過
        print("往右排序的過程:",nLst)
        if not is_sorted:
            break  #跳出while loop

        end=end-1
        for i in range(end-1,start-1,-1): #往左邊了
              if(nLst[i]>nLst[i+1]): #如果左邊元素於右邊
                nLst[i],nLst[i+1]=nLst[i+1],nLst[i]
                is_sorted=True #排過
        start=start+1
        print("往前排序的過程:",nLst)
    return nLst

data=[6,1,5,7,3]
print("原始串列",data)
print("排序結果:",cocktail_sort(data))
