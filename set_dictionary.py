#set 集合,一群沒有順序的資料
#集合的運算
#s1={3,4,5}
#print(3 in s1)
#print(10 in s1)
#print(10 not in s1)

s1={3,4,5}
s2={4,5,6,7}
#s3=s1&s2  #交集: 取兩個集合中交集的資料
#print(s3)

#s3=s1|s2  #聯集 :取兩集合中 所有資料,但不重複
#print(s3)

#s3=s1-s2  #差集 從s1中減去與s2中有重疊的部分
#print(s3)

#s3=s1^s2 #反交集: 取兩個集合中,不重疊的部分
#print(s3)

#s=set("Hello") # set(字串) 把字串拆成集合,無順序性,並且不重複
#print(s)
#print("H" in s) #判斷H是否在集合中

#字典的運算 : key-value 配對   一樣用大括號
dic={"apple":"蘋果","bug":"蟲蟲"} 
#dic["apple"]="小蘋果"
#print(dic["apple"]) #先用變數dic取得字典,再用鍵取得值
print("apple" in dic) #判斷key是否存在
print("test" not in dic) #判斷test(key)是否存在
print(dic) #印出dic
del dic["apple"]  #刪除字典中的鍵值對(key-value pair)
print(dic)

#利用列表的資料去產生字典
dic={x:x*2 for x in [3,4,5]}  #[]就是一個列表
print(dic) #x的值從列表進來, 把列表轉換成鍵值對

#總結,以列表的資料當基礎,去產生子字典

