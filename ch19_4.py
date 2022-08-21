#利用輾轉演算法計算gcd
def gcd(n1,n2):
    #首先大的數字要先放前面  要先判斷
    if n1<n2:
        n1,n2=n2,n1  #交換位置
    while n2!=0:
        remainder=n1%n2
        n1=n2
        n2=remainder
    return n1  #gcd number





#let user input two numbers
n1,n2=eval(input("please input two numbers"))
print("the gcd is ",gcd(n1,n2))
