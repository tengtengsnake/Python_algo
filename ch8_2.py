phone_book={}  #建立通訊錄的字典
phone_book['Trump']='0912111111'
phone_book['Lisa']='0922222222'
phone_book['Mike']='0932333333'
name=input("請輸入名字:")
if name in phone_book:
    print('{}的電話號碼是{}'.format(name,phone_book[name]))
else:
    print("{}不在通訊錄中".format(name))
