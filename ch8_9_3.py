#建立月份的hashtable
while True:
    input_month=input("請輸入英文月份(會輸出中文月份):")
    month_hash_table={}
    month_hash_table['January']='一月'
    month_hash_table['Fabuary']='二月'
    month_hash_table['March']='三月'
    month_hash_table['April']='四月'
    month_hash_table['May']='五月'
    month_hash_table['June']='六月'
    month_hash_table['July']='七月'
    month_hash_table['August']='八月'
    month_hash_table['September']='九月'
    month_hash_table['October']='十月'
    month_hash_table['November']='十一月'
    month_hash_table['December']='十二月'
    #print(month_hash_table)
    if input_month in month_hash_table:
        print(month_hash_table[input_month])
    else:
        print("輸入錯誤,請重新輸入")
