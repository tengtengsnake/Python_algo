def check_name(name):
    if voted[name]:
        print("你已經投過票摟")
    else:
        print("歡迎投票")
        voted[name]=True
voted={}  #建立選民名單
voted={'Trump':None,'Lisa':None,'Mike':None}
name=input("請輸入名子:")
if name in voted:
    check_name(name)
else:
    print("你不是選民")
