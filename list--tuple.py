#有序可變動列表  List
grades=[12,52,41,63,54]
print(grades[2])
#更新資料的示範
grades[0]=6
print(grades[0])
print(grades)
print(grades[1:4])
#利用以上方法也可把列表便空白
grades[1:4]=[]  #連續刪除列表中從1到4(不包含)的資料,設定為空
print(grades)
#列表簡單的串接
grades=grades+[12,33] #原來的列表加上新的列表 先看等號右方
print(grades)
#找尋列表的長度,利用len找尋列表的長度
length=len(grades)
print(length)
#有序不可變動列表 Tuple