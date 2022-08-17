voted={} #先建立一個空的投票字典

def check_name(name):
    if name in voted:
        print("您已經投過票摟")
    else:
        voted[name]=True
        print('歡迎投票')
while True:        
    name=input("請輸入名子:")
    result=check_name(name)

    
