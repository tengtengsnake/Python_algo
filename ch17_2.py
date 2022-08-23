abc='abcdefghijklmnopqrstuvwxyz'
encry_dict={}
front3=abc[:3]   #abc
end23=abc[3:]    #d~z
subText=end23+front3
encry_dict=dict(zip(abc,subText))
print("列印編碼字典\n",encry_dict)
msgTest=input("請輸入原始字串/明文")

cipher=[]
for i in msgTest:
    v=encry_dict[i]
    cipher.append(v)
ciphertest=''.join(cipher) #將串列轉成字串

print("plain-text",msgTest)
print("cipher-test",ciphertest)
