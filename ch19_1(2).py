def isPrime(num):
    for n in range(2,num):
        if num%n==0:
            return False
        else:
            return True
num=int(input("請輸入大於1的整數做prime number test"))
if isPrime(num):
    print("%d is a prime number"%num)
else:
    print("%d is not a prime number"%num)
