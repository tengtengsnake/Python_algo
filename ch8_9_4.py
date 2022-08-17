import hashlib
input_school_name=input("請輸入學校名稱:")
data=hashlib.md5() #建立data 物件,in order to use the md5() in class hashlib
school=input_school_name
data.update(school.encode('utf-8')) #更新data 物件內容
#print("Hash Value        ",data.digest())
print("Hash Value(16進位):",data.hexdigest())
