#Prime number test
# the condition of a prime number is 1: 2 is a prime number,2: prime number 的因數只能有1與自己   也可以這樣說n不可被2至n-1的數字整除
def isPrime(num):
    '''test num is a integer or not'''
    if(num%2==0): #如果number取餘數=0 代表整除
        return False  #整除,所以不是一個prime number
    else:
        return True


num=int(input("請輸入一個數字"))
if isPrime(num):
    print("num is a prime number")
else:
    print("num isn't a prime number")
