def factorial(N):
    '''factorial review and rethink'''
    if N==1:
        return 1
    else:
        return N*factorial(N-1)
N=eval(input("請輸入一個數字："))
print(N,'的階乘結果是:',factorial(N))
