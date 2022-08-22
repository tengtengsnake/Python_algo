#使用sha256() 測試兩個類似字串產生完全不同的hashcode
import hashlib

data1=hashlib.sha256()  #利用類別建立物件
data1.update(b'Ming-Chi Institute of Technology')  #更新物件內容
print("Hash Value=",data1.hexdigest())  #generate the hashcode

data2=hashlib.sha256()
data2.update(b'ming-Chi Institute of Technology')
print("Hash Value=",data2.hexdigest())
