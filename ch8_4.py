import hashlib   #使用python builtin 的hashlib 裡面有提供雜湊演算法,MD5(message digest 5),SHA1(secure hash algo),SHA224,SHA256,SHA384,SHA512 
data=hashlib.md5() #建立data 物件
data.update(b'Ming-Chi Institute of Technology')  #b 表示轉成二進位 0,1. 更新data 物件內容

print('Hash Value          =',data.digest)
print('Hash Value(16進位)=',data.hexdigest())
print(type(data))
print(type(data.hexdigest()))
