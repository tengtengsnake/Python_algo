def factorial(n):
    '''計算n的階乘'''
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
N=eval(input("請輸入階乘數:"))
print("N的階乘結果是：",factorial(N))
