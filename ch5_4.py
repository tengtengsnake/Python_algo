#電腦語言在使用函數呼叫時,是使用堆疊在運作  
def bye():
    print("下回見！")
def system(name):
    print("%s歡迎進入淡江校友會系統"%name)
def welcome(name):
    print("%s歡迎進入淡江校友會系統"%name)
    system(name)
    print("使用淡江大學校友會系統很棒")
    bye()
welcome("蔡沛騰")
