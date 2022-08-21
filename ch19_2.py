#回文Palindrome 右pop() = popleft()
from collections import deque

def palindrome(word):
    wd=deque(word) #打出queue
    while len(wd)>1:
        if wd.pop()==wd.popleft():#pop 從末端讀取queue資料,popleft() 則是從左端讀取queue資料
            return True
        else:
            return False
print("x is palindrome:",palindrome("x"))
print("abccba is palindrome",palindrome("abccba"))
print("radar is palindrome",palindrome("radar"))
print("python is palindrome",palindrome("python"))
