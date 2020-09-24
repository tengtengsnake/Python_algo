#巢狀列表 
#data=[[3,4,5],[6,7,8]]
#print(data)
#print(data[1][2]) #印出巢狀列表,第一層第一個 是3
#data[0][0:2]=[5,5,5]  #代表[3,4,5] 這邊把3,4換成5,5,5 在加回原本的5變四個5
#print(data)

#有序不可更動列表 Tuple  這邊注意 使用小括號
data=(3,4,5)
print(data[0:2])   #印出索引值 
data[0]=5  #錯誤 tuple 的資料不可變動
print(data)





