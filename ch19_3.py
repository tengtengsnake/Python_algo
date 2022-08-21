#毆幾里得演算法
#目的:主要是可以解決土地規劃問題,假設有一塊長寬（40,16),的土地,要將之切成正方形,且不能浪費土地,求其正方形最大邊長
#利用最大公因數(Greatest common divisor)求解
def gcd(n1,n2):
    g=1 #先設兩數最大公因數是1
    n=2 #從2開始檢測
    while n<=n1 and n<=n2:
        if (n1%n==0 and n2%n==0):
          g=n
        n+=1
    return g
n1,n2=eval(input("請輸入兩個數字"))
print("最大公因數是:",gcd(n1,n2))
