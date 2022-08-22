import hashlib

def create_password(pwd):
    data=hashlib.sha256() #建立物件
    data.update(pwd.encode('utf-8'))  #把收到的密碼轉換成hashcode
    return data.hexdigest()

acc=input("請建立新帳號")
pwd=input("請輸入密碼")
account={}  #建立密碼字典 紀錄帳號跟hashcode
account[acc]=create_password(pwd) #建立key value pair

print("歡迎進入系統")
userid=input("請輸入帳號:")
password=input("請輸入密碼")
if userid in account:
    if create_password(password)==account[userid]:
        print("歡迎使用本系統")
    else:
        print("密碼錯誤")
else:
    print("帳號錯誤")

