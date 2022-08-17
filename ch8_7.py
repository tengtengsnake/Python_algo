import hashlib

data=hashlib.sha1()  #建立data物件
data.update(b'Ming-Chi Institute of Technology') #更新data物件內容

print('Hash value       =',data.digest())
print('Hash Value(16)進位:',data.hexdigest())
print(type(data))
print(type(data.hexdigest()))
