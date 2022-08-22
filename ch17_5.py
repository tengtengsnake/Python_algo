import hashlib

data=hashlib.sha256()  #建立物件 使用hashlib.sha256() 類別建立物件
data.update(b'Ming-Chi Institute of Technology')
print(type(data))
print(data.hexdigest())
print(len(data.hexdigest()))
