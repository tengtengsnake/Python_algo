# python_algo_relative knowledge. 
## Script language（腳本語言)  
+ 是個文字式（text-based）的語言  
+ 為了縮短傳統的「編寫、編譯、連結、執行」（edit-compile-link-run）過程而建立的電腦語言 
+ 以簡單的方式快速完成某些複雜的事情通常是腳本語言的重要原則  
+ 
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
+ FILO(First in last out) 結構    
+ recursive call 就是使用stack  
+ 無法讀取中間的資料  
+ 利用List來實作stack  
+ 內建方法實踐push/pop. ->append()/pop()  
### Binary Tree 二元樹  
+ 每一個節點可以儲存3個資料,分別是data,left pointer,right pointer  
+ 如果一個節點他完全沒有子節點,便可稱此節點為**葉節點(leaves node)**  
+ 使用陣列儲存二元樹  
#### 樹的種類  
![](https://miro.medium.com/max/1200/1*CMGFtehu01ZEBgzHG71sMg.png)
+ 以層次定義樹的深度,往下越深,每i層最多有2**(i-1)個節點  
+ 滿元樹(Full binary tree),是指除葉節點沒有子節點,其他都有節點的有兩個子節點  
![](https://web.ntnu.edu.tw/~algo/BinaryTree2.png)
+ 完全二元樹(Complete binary tree),
![](https://cdn.programiz.com/sites/tutorial2program/files/complete-binary-tree_0.png)
+ 平衡樹(Balanced binary tree),每個節點的兩個子節點深度不可以超過1  
![](https://media.geeksforgeeks.org/wp-content/uploads/tree.jpg)
+ 完美二元樹(Perfect Binary tree),除最深層節點,其他節點都是滿的
![](https://cdn.programiz.com/sites/tutorial2program/files/perfect-binary-tree_0.png)
### 資料安全與資料加密  (認識專有名詞)  
+ 竊聽(wiretap)  傳送方A傳遞資訊給接收方B的過程中被C擷取,就是竊聽wiretap ,可以透過資料加密解決 
![](https://camel.apache.org/components/3.18.x/eips/_images/eip/WireTap.gif)  
+ 竄改(tamper) 避免傳遞的資料被擷取後竄改,可以用**數位簽章**,**訊息鑑別碼**解決  
+ 電子詐騙(E fraudf) 傳送方A被駭客偽裝  
+ 拒絕(repudiation) 傳送方A沒有事先跟Ｂ說要傳送資訊,造成糾紛  
+ 明文/原始文件(plain text) ,沒有加密過的資料  
+ 密文(cipher text) 加密過的資料  
+ 加密就是將數據轉換成一般人難以理解的內容,採用的方法稱之為金鑰  
#### 摩斯密碼 Morse code  
![](https://as1.ftcdn.net/v2/jpg/01/68/20/26/1000_F_168202614_Jj43C5BwxvuulH5GExEc9fAhvXyN9vrJ.jpg)
+ 時通時斷訊號代碼,使用無線電傳輸  
+ 在python中,是利用字典來建立morse code的,可以利用迴圈將使用者輸入的key值把對應的value迭代出來  
#### [凱薩密碼( Caesar cipher )](https://ithelp.ithome.com.tw/m/articles/10261660)    
![](https://i.imgur.com/Z2Erlgil.png)  
+ 做法是將每一個英文字母都往後推n個，上圖表示為 n=2 ( 而凱薩使用的是n=3 )  
+ 編碼 ( encode ):編碼是把資料換個表示方法儲存  
+ 像ASCII、UTF-8、base64、甚至摩斯密碼等也都是編碼方式
+ 但是編碼不具已有保護資料功能    
![](https://chart.googleapis.com/chart?cht=tx&chl=E(x)%20%3D%20(x%2Bn)%20mod%2026)
![](https://chart.googleapis.com/chart?cht=tx&chl=D(x)%20%3D%20(x-n)%20mod26)
### [Hash table](https://hackmd.io/@jkrvivian/HJln3jU_e?type=view)  
![](https://khalilstemmler.com/img/blog/data-structures/hash-tables/hash-table.png)
+ 主要目的是提高搜尋某一個元素的效率  
+ 利用python 中的dict{key:value} pair,只要有key就可以得到value -> time compleity O(1)  
+ 當字串經過hashfunction得到hashcode,再利用hashcode%n(n是陣列長度) 就可以得到index value  
+ index=hashcode%n  
+ 當兩字串index 相同時,此時會發生碰撞,必須用鏈結法chaining 處理  使用線性探測法(linear probing)找尋index 相同的字串  
+ 負載係數(loadfactor):評估table使用情況,是否要擴充table或是使用新table     
+ 一般商用資料庫系統是將使用者建立的密碼送到雜湊函數產生hashcode,所以即使hashcode被盜或外洩,使用者密碼不用擔心被逆推
#### md5(message digest 5)訊息摘要  
+ 又稱訊息摘要演算法  
+ 將文字轉成固定128位元的長度的值  
+ 不建議使用,已被破解  
#### SHA(Secure hash algo)家族  
![](https://slidesplayer.com/slide/11296650/61/images/21/SHA%E5%AE%B6%E6%97%8F+%E6%BC%94%E7%AE%97%E6%B3%95+%E8%BC%B8%E5%87%BA%E9%9B%9C%E6%B9%8A%E5%80%BC%E9%95%B7%E5%BA%A6+%28bits%29+%E4%B8%AD%E7%B9%BC%E9%9B%9C%E6%B9%8A%E5%80%BC%E9%95%B7%E5%BA%A6+%28bits%29+%E8%B3%87%E6%96%99%E5%8D%80%E5%A1%8A%E9%95%B7%E5%BA%A6+%28bits%29+%E6%9C%80%E5%A4%A7%E8%BC%B8%E5%85%A5%E8%A8%8A%E6%81%AF%E9%95%B7%E5%BA%A6+%28bits%29.jpg)
+ 由NSA(national secure agency) 設計 NIST(National insiture of standards and Technology) 發布    
+ 種類有SHA-0,SHA-1(被破解),SHA2,SHA3  
##### [SHA2 SHA256](https://shattered.io)  
+ 廣泛使用,尚未破解  
### 什麼是碰撞抵抗?  
![](https://inside-assets1.inside.com.tw/2017/02/Collision-illustrated.png?w=730&fit=max&q=80)
+ [雜湊碰撞](https://www.inside.com.tw/article/8614-google-just-had-first-sha-1-collision)（hash collision，即兩個不同檔案雜湊表一致，也有譯作雜湊衝突）本來不應該發生
+ ![](https://inside-assets1.inside.com.tw/2017/02/shattered-infographic.png?w=730&fit=max&q=80)
#### 金鑰密碼  
+ 實務應用上可以將加密與解密分成兩種 1:對稱金鑰密碼(symetric-key algo),2:公開金鑰密碼(public key cryptography)  
+ 對稱金鑰密碼又稱為對稱加密,使用相同金鑰來處理加解密  ,但會有金鑰傳送困難的問題,金鑰傳送過程中可能會被劫去  金鑰是非公開  
+ 非對稱金鑰密碼(Asymmetric crytpgraphy)又稱為公開金鑰密碼,主要有兩個金鑰用於加密(公開)與解密(非公開)  因使用不同金鑰加密與解密,所以稱為非對稱加密 ex:RSA演算法  
+ RSA的問題不知道會不會被中間人攻擊(man in the middle attack) MITI  ,公鑰私鑰都是由接收方給傳送方,給公鑰的途中可能會被駭客換成自己的公鑰  
#### 訊息鑑別碼(Message authoentication code)  
+ 簡稱MAC碼  
+ 其實就是checksum拉
+ 經由MAC algo 產生MAC碼,其實就是經過hash-function 產生hashcode(checksum)   
#### 數位簽章(Digital Signature)  
+ 像是在文件上簽名的技術
+ 具有確認身份,以及文件完整性  
+ 使用**私鑰**加密,,想像成簽名拉,使用公鑰解密,相當於驗證簽名  
+ 驗證簽名,收的一方必須知道簽名長怎樣,傳送方必須事先讓接收方知道    
#### 數位憑證(Digital certificate),又稱身份憑證(identity certificate)  
+ 主要是用來認證使用者身份,由CA(certificate authority)負責通訊方身份認證  
### 排序Sort  
+ 將一串資料依特定方式排序  
+ 輸出結果是遞增序列(如果沒有註明是反向排序(reversed sort)   
+ 排序可以是數字或字串  
#### 氣泡排序法(Bubble sort)  
![](https://static.studytonight.com/data-structures/images/basic-bubble-sort.png)  
+ 最著名,最簡單  
+ 將相鄰元素作比較,如果前一個元素大於後一個,將兩者位置交換  
+ 如果有n筆元素,將做n-1次比較(n-1次迴圈)  
+ time complexity is O(n**2)  
#### 雞尾酒排序法(Cocktail sort)  
![](https://img.magiclen.org/albums/cocktail-sort/animation-541x176.gif)
+ 為bubble sort() 改良版
+ also known as bidirectional bubble sort  
+ 元素沒有更動,即資料完成排序  
+ time complexity 最佳是O(n),平均是O(n**2)  
+ 
#### 選擇排序法 (Selection sort)  
![]([http://i.stack.imgur.com/qa2Cg.gif](https://ithelp.ithome.com.tw/upload/images/20211003/20121027Z3FUzMHujx.jpg))  
+ 原理是反覆從未排序數列中找出最小值，將它與左邊的數做交換。可以有兩種方式排序，一為由大到小排序時，將最小值放到末端;若由小到大排序時，則將最小值放到前端  
+ n=5
第1回合在4個數中找最小值，找4次，n-1次  
第2回合在3個數中找最小值，找3次，n-2次  
第3回合在2個數中找最小值，找2次，n-3次  
第4回合在1個數中找最小值，找1次，n-4次  
總共找了4回合，n-1回合  
  
(n-1) + (n-2) + .... + 1 = n(n-1) / 2  
平均時間複雜度為: O(n²)  
#### 合併排序法(Ｍerge sort)  
![](https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/Sorting%20series/ComparisonSort_fig/MergeSort/f1.png?raw=true)
+ Merge Sort屬於Divide and Conquer演算法，把問題先拆解(divide)成子問題，並在逐一處理子問題後，將子問題的結果合併(conquer)，如此便解決了原先的問題。
+ 以圖一為例，要把數列{5,3,8,6,2,7,1,4}排序成{1,2,3,4,5,6,7,8}，Merge Sort的方法為：  
Divide：把數列「對半拆解」成兩個小數列。
先把{5,3,8,6,2,7,1,4}分成{5,3,8,6}與{2,7,1,4}。  
再把{5,3,8,6}分解成{5,3}與{8,6}。  
{2,7,1,4}分解成{2,7}與{1,4}。  
依此類推，直到每個數列剩下一個元素。  
Conquer：按照「由小到大」的順序，「合併」小數列。  
考慮數列{5}與{3}，比較大小後，合併成數列{3,5}。  
考慮數列{8}與{6}，比較大小後，合併成數列{6,8}。  
考慮數列{3,5}與{6,8}，比較大小後，合併成數列{3,5,6,8}。  
依此類推，最後，考慮數列{3,5,6,8}與{1,2,4,7}，比較大小後，合併成數列{1,2,3,4,5,6,7,8}。  
### KNN 演算法(K-Nearest Neighbor)  K-鄰演算法  
+ 用於**分類**以及**回歸**  
+ 利用dist 值的大小判斷兩者差異程度,值越小差異越少 使用畢氏定理觀念  
+ 可用於影片推薦  
### 職場面試題目  
+ 歐幾里得演算法  
#### 找到最大公因數 兩種方式 輾轉相除法,lcm method
+ 利用 (Euclidean algorithm)輾轉演算法比較容易  
+ ![](https://cdn.inchcalculator.com/wp-content/uploads/2018/12/euclids-algorithm.png)
+ LCM method 找尋
![](https://d138zd1ktt9iqe.cloudfront.net/media/seo_landing_files/greatest-common-divisor-using-lcm-method-1621833508.png)

#### 找到最小公倍數  LCM(least common multiple)  
+ LCM method   兩數相乘除以gcd  

## Graph 圖論  
+ basic graph 只有節點(vertices)以及邊(edge)組成  
![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/undirectedgraph.png)
+ 生活實例 臉書朋友關係可以使用圖型表達  
![](https://images.saymedia-content.com/.image/t_share/MTczODc5ODgzMjA0OTk0MTEy/how-i-track-down-old-friends-on-facebook.jpg)
+ 上圖中,每一個節點表示ㄧ個人,頂點之間有線連接表示是相鄰節點,有些是直接朋友關係,有些則不是  
+ 加權圖形 
![](https://i.stack.imgur.com/Mu6VZ.png)
＋ 在上圖中,可以在邊上加上數字表示權重,表示頂點之間的連線關係  
![](https://www.oreilly.com/library/view/a-common-sense-guide/9781680502794/images/chapter14/graphs_second_half_Part8.png)
+ 此圖頂點之間的數字可以表示城市之間的距離  
+ Directed graph 有向圖形  頂點之間的連線(邊)具有方向性  
![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Directed_graph%2C_cyclic.svg/450px-Directed_graph%2C_cyclic.svg.png)
+ Directed Acycle Graph  有無環圖  簡稱DAG 無法找到頂點可以經由連接線返回此頂點
![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Directed_acyclic_graph_3.svg/1200px-Directed_acyclic_graph_3.svg.png)
+ Topological Sort 拓墣排序,如果有一個圖的節點之間有順序關係,我們可以稱此圖為**拓墣排序**  
## Heap 堆積  
+ 最大堆積(max heap),父節點永遠大於子節點  
+ 最小堆積(min heap),父節點永遠大於子節點  
## 決策樹(Decision Trees,DT)  
+ 可以應用在回歸或是分類問題,所以有時也稱作(Classification And Regression,CART)    
+ 有點像是一堆if-else敘述進行連接,直到最後得到想要的結果    
+ 特徵節點選擇不同時,可以生成很不一樣的DT  
+ 理論上DT能達到100%準確率,只要樹的深度夠深  
+ 決策樹非常容易過擬合,即使在訓練時準確率很高,但在測試集會出事拉～準確率會顯著下降  
+ overfit解決辦法是為這棵樹進行修剪,叫做pruning(剪支),有兩種方式,1:先剪枝,2:後剪枝  
+ 缺點:不適合多特徵複雜的分類問題  
## 熵(entropy)  
+ 資訊熵:代表隨機變數的複雜度,也就是不確定性    
+ 條件熵:代表在某一個條件下,隨機變數的複雜度  
