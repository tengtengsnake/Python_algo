# modify from the ch1_1.py
def factorial(n):
    global fact
    if n==1:
        print("factorial(%d)呼叫前%d!=%d"%(n,n,fact))
        print("到達遞迴條件終止 n=1")
        fact=1
        print("factorial 返回後 %d!=%d"%(n,n,fact))
        return fact
    else:
        print("factorial(%d)呼叫前%d!=%d"%(n,n,fact))
        fact=n*factorial(n-1)
        print("factorial 返回後 %d!=%d"%(n,n,fact))
        return fact
fact=0
N=eval(input("請輸入數字"))
print(N,"階乘數是：",factorial(N))
