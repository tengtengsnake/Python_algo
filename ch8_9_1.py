phone_book={} #建立空字典
phone_book['Trump']='0912111111'
phone_book['Lisa']='0922222222'
phone_book['Mike']='0932333333'
phone_book['Emergency']='119'  #新增一個key value pair
name=input("請輸入名稱:")
if name in phone_book:
    print('{}的電話號碼是{}'.format(name,phone_book[name]))
else:
    print('{}不在通訊錄中'.format(name))
