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


