#迴圈搭配的指令 break&continue
#強制結束迴圈
    # while boolean value:
    #     break
    # for變數名稱in列表或字串:
    #     break    

    #example
    # n=1
    # while n<5:
    #     if n==3:
    #         break
    #     n+=1
    # print(n)  


    #break的簡易範例
n=0
while n<5:
  if n==3:
      break
  n+=1  
  print(n)#印出所有的 n
print("最後的 n: ",n) #印出迴圈最後的n    


