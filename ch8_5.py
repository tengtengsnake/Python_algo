import hashlib

data=hashlib.md5()   #建立data物件
school='明志科技大學'  #中文字串
data.update(school.encode('utf-8'))#更新data物件
 
print('Hash Value          =',data.digest()) 
print("Hash Value(16進位)=",data.hexdigest())
print(type(data))
print(type(data.hexdigest()))
