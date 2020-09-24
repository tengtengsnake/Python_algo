#迴圈

#while :

#for變數名稱 in 列表或字串 : 將列表中的字串或項目逐一取出,逐一處理  
# for x in [4,1,2]
#     print("逐一取得列表資料",x)
#     #使用range() 經常與for()搭配使用
#     ex:for x in range(3):
#     =
#        for x in [3,4,5]

# while 迴圈
# n=1
# while n<=3: #boolean value 
#     print(n)
#     n+=1

#搞一個等差級數加法 ex:1+2+3+4+...+10
#sum=0 #用來記錄累加的結果
# n=1
# sum=0
# while n<=10:
#     sum=sum+n
#     n+=1    
# print(sum)
   
#space buttton is quite different to the  tab button ,they are different here
# for 迴圈

# for x in range(5): #range(5)相當於一個[0,1,2,3,4]的一個列表
# for x in range(5,10):#range(5,10)=[5,6,7,8,9]的一個列表
#     print(x)

sum=0
for x in range(1,11): #取列表中1到10
    sum=sum+x
print(sum)    


