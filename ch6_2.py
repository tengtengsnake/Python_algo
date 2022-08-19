def create_btree(tree,data):
    '''使用data建立二元樹'''
    for i in range(len(data)): #len(data)=6
        level=0
        if i==0:
            tree[level]==data[i]
        else:
#當while迴圈結束表示找到存放數據的節點(索引)位置
            while tree[level]:  #節點標示
                if data[i]>tree[level]: #比較新進來的data跟節點表示進行大小比較
                    level=level*2+2
                else:
                    level=level*2+1
        tree[level]=data[i]
#print(i,tree)
btree=[0]*8 #建立一個有8個元素的陣列(串列)
data=[10,21,5,9,13,28]  #建立data串列
create_btree(btree,data)
for i in range(len(btree)):
    print("二元樹陣列btree[%d]=%d"%(i,btree[i]))
    
