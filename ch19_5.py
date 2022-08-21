#gcd with lcm
#輾轉相除法
from math import remainder


def gcd(n1,n2):
    #大數放前
    if n1<n2:
        n1,n2=n2,n1
    while(n2!=0):
        remainder=n1%n2
        n1=n2
        n2=remainder
    return n1


#additional part
#lcm least common multiple
def lcm(a,b):
    result=(a*b)/gcd(a,b)
    return result


n1,n2=eval(input("please input two numbers"))
print("the gcd is",gcd(n1,n2))
print("the lcm number is",lcm(n1,n2))
