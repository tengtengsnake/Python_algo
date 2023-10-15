num_list = [1,2,3,4,5,6,7]

# 為num_list標記index
low = 0 # 所以num_list[low] = 1
high = len(num_list)-1 # high是6，所以num_list[high] = 7

find_value = 6 # 假設我要找6在哪裡

while low <= high:
    mid = (low + high) / 2 # mid =3，所以一開始是num_list[3] = 4
    mid = math.floor(mid)

    if(find_value > num_list[mid]): # 代表要找的值會在右半邊，所以下一次尋找會從右半邊開始找，也就是4的旁邊 5,6,7這個右半區域開始尋找，所以區間會從index 0~6變成4~6 所以將low = mid+1 變成4
        low = mid+1 
    elif(find_value< num_list[mid]): # 代表要找的值會在左半邊 
        high = mid-1 # 區域變成0~2 high從原本的index 6變成2  low = 4 , high = 6 mid = 5
    else:
        break # 最後上面都不成立 所以break跳出迴圈 並且找到目標值
print("目標值{}在索引{}的位址".format(find_value,mid))
