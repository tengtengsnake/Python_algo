# use the remove() to delete element from the array
# 使用remove(x)方法刪除指定陣列第一個出現的元素x
from array import*
x=array('i',[5,15,25,35,45])
x.remove(25)
for data in x:
    print(data)
