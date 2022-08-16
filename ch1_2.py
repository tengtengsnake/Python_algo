from itertools import combinations


def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
N=eval(input('請輸入一個數字:'))
times=10000000000000 #假設電腦每秒可以處理10兆個數列
day_secs=60*60*24  #一天有24小時,24*60分鐘,24*60*60秒
year_secs=365*day_secs  #一年總秒數
combinations=factorial(N) #組合數
years=combinations/(times*year_secs)
print('資料個數%d,數列組合數=%d'% (N,combinations))
print('需要%d年才可以獲得結果'% years)

#列舉方法(enumeration method)超慢但一定可以找到答案
