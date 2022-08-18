# python_algo_practice
## 時間複雜度
![](https://i.ytimg.com/vi/47GRtdHOKMg/maxresdefault.jpg)  
+ 因為每一台電腦效能不同,因此科學家不會採用絕對時間來衡量code所執行得時間
+ 時間複雜度(time complexity) 簡化原則是1.常數用1表示,2.省略係數,3.保留最高階項目  
## 空間複雜度  
+ 程式執行所需記憶體空間. 
+ 通常時間比起記憶體空間成本來說更加重要,有些書甚至沒有提到space complexity  
+ factorial 使用(recursive call)遞迴式呼叫,使用stack並且是last in first out 結構  
## 資料結構  
+ 資料在記憶體中擺放的位置,不同的位置將會大大影響存取資料的時間成本  
### 陣列(array)  
![](https://www.marcinkossakowski.com/images/data-structures/array.png)
+ 電腦記憶體是一塊連續的儲存空間  
+ 陣列中的資料稱之為元素  
+ 要存取元素使用索引來存取,此種存取方式又稱為隨機存取(random access)  
+ 只需要一個步驟就可以取得陣列元素內容所以->time complexity O(1)  
#### insert/delete 元素    
+ 插入資料時,有可能要移動所有元素 檢視所有元素 ->time complexity O(n)  
+ 要先確定後方有無空間,將其他元素往後移動,才能將新元素插入  
+ 沒有空間,則必須找尋更大的記憶體空間,並且連同原本陣列一起轉移 ->time complexity O(n)  
+ 刪除元素,則是後方元素往前移動-> time complexity O(n)  
+ 搜尋元素 ->time complexity O(logn) 二分法  
### 鏈結串列linked_list. 
![](http://www.geeksforgeeks.org/wp-content/uploads/gq/2013/03/Linkedlist_insert_last.png)
+ 讀取資料使用順序讀取(sequential access)  
+ 不必在連續記憶體空間  
#### 插入/刪除 節點  
+ ->time complexity O(1)  
#### 循環鏈結串列(circle linked list)  
![](https://media.geeksforgeeks.org/wp-content/uploads/CircularSinglyLinkedList.png)
+ 設計將末端節點指向頭節點,就是一個circle lineked list  
#### 雙向鏈結串列(double linked list)   
+ 多一個指標區,設計用來指向前面一個節點

### Queue 
![](https://media.geeksforgeeks.org/wp-content/uploads/geek-queue-1.png)
+ 資料插入/讀取 enqueue/dequeue 使用insert() 以及pop() 打出尾部資料   
+ 線性資料結構 queue就是排隊拉,FIFO先進先出  
+ 讀取資料觀念dequeue,讀取後在移除,也可稱為取出資料  
+ 因為是FIFO,所以無法讀取中間的資料
### Stack 堆疊  
![](https://miro.medium.com/max/1400/0*ODLWiNnxC-G1Wf5P.png)
+ 也是線性資料結構,特色:由下往上進行資料堆疊  
+ FIFO(First in last out) 結構    
+ recursive call 就是使用stack  
+ 無法讀取中間的資料  
+ 利用List來實作stack  
+ 內建方法實踐push/pop. ->append()/pop()  
### [Hash table](https://hackmd.io/@jkrvivian/HJln3jU_e?type=view)  
![](https://khalilstemmler.com/img/blog/data-structures/hash-tables/hash-table.png)
+ 主要目的是提高搜尋某一個元素的效率  
+ 利用python 中的dict{key:value} pair,只要有key就可以得到value -> time compleity O(1)  
+ 當字串經過hashfunction得到hashcode,再利用hashcode%n 就可以得到index value  
+ index=hashcode%n  
+ 當兩字串index 相同時,此時會發生碰撞,必須用鏈結法chaining 處理  使用線性探測法(linear probing)找尋index 相同的字串  
+ 負載係數(loadfactor):評估table使用情況,是否要擴充table或是使用新table     
+ md5(message digest 5)訊息摘要  


