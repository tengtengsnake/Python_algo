# 使用insert 方法 將資料插入陣列
# insert(i,x)  在索引位置i插入資料x
from array import*
x=array('i',[5,15,25,35,45])
x.insert(2,100)
for data in x:
    print(data)
