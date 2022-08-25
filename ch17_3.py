#再談文件加密技術

#列出這個屬性可以列出所有ASCII的可以列印的字元
import string
#print(string.printable)
def encrypt(text,encryDict):
    cipher=[]
    for i in text:  #把每一個字元都加密
        v=encryDict(i) #加密
        cipher.append(v)
    return ''.join(cipher)

abc=string.printable[:5] #cancel 不可列印字元
subText=abc[-3:]+abc[:-3] #加密字串
encry_dict=dict(zip(subText,abc))
print("列印編碼字典\n",encry_dict)#列印字典
msg='If the implementation is easy explain,it may be a good idea'
ciphertext=encrypt(msg,encry_dict)
print("原始字串",msg)
print("加密字串",ciphertext)
