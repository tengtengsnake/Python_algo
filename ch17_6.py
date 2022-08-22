import hashlib

data=hashlib.sha256()  #建立物件 使用hashlib.sha256() 類別建立物件
data.update(b'Ming-Chi Institute of Technology')
print(type(data))
print(data.hexdigest())
print(len(data.hexdigest()))
#必須建立一個物件,之後更新這個物件的內容,搭配使用hexdigest() 得到16進位的hashcode
