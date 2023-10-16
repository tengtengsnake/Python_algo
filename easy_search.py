# 簡易搜尋

num_list = [1,2,3,4,5,6,7]

low_index = 0 # 6
high_index = len(num_list)-1 # 6

find_value = 7

while(low_index <= high_index):
    if(num_list[low_index] != find_value):
        low_index += 1
    else:
        print("Get the target value with: {} at index {}\n ".format(find_value,low_index))
        break
 
