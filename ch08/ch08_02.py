MAXSIZE=10  #定義佇列的最大容量	

front=-1 #指向佇列的前端
rear=-1 #指向佇列的後端

class Node:
    def __init__(self,x):
        self.x=x   #頂點資料
        self.next=None  #指向下一個頂點的指標
        
class GraphLink:
    def __init__(self):
        self.first=None
        self.last=None
        
    def my_print(self):
        current=self.first
        while current!=None:
            print('[%d]' %current.x,end='')
            current=current.next
        print()

    def insert(self,x):
        newNode=Node(x)
        if self.first==None:
            self.first=newNode
            self.last=newNode
        else:
            self.last.next=newNode
            self.last=newNode
 
#佇列資料的存入
def enqueue(value):
    global MAXSIZE
    global rear
    global queue
    if rear>=MAXSIZE:
        return
    rear+=1
    queue[rear]=value
    

#佇列資料的取出
def dequeue():
    global front
    global queue
    if front==rear:
        return -1
    front+=1
    return queue[front]

#廣度優先搜尋法
def bfs(current):
    global front
    global rear
    global Head
    global run
    enqueue(current) #將第一個頂點存入佇列
    run[current]=1 #將走訪過的頂點設定為1
    print('[%d]' %current, end='') #印出該走訪過的頂點
    while front!=rear: #判斷目前是否為空佇列
        current=dequeue() #將頂點從佇列中取出
        tempnode=Head[current].first #先記錄目前頂點的位置
        while tempnode!=None:
            if run[tempnode.x]==0:
                enqueue(tempnode.x)
                run[tempnode.x]=1 #記錄已走訪過
                print('[%d]' %tempnode.x,end='')
            tempnode=tempnode.next

#圖形邊線陣列宣告
Data=[[0]*2 for row in range(20)]

Data =[[1,2],[2,1],[1,3],[3,1],[2,4], \
       [4,2],[2,5],[5,2],[3,6],[6,3], \
       [3,7],[7,3],[4,5],[5,4],[6,7],[7,6],[5,8],[8,5],[6,8],[8,6]]

run=[0]*9 #用來記錄各頂點是否走訪過
queue=[0]*MAXSIZE
Head=[GraphLink]*9
 			
print('圖形的鄰接串列內容：') #列印圖形的鄰接串列內容
for i in range(1,9):  #共有8個頂點
    run[i]=0 #設定所有頂點成尚未走訪過
    print('頂點%d=>' %i,end='')
    Head[i]=GraphLink()
    for j in range(20):
        if Data[j][0]==i: #如果起點和串列首相等，則把頂點加入串列
            DataNum = Data[j][1]
            Head[i].insert(DataNum)
    Head[i].my_print()#列印圖形的鄰接串列內容

print('廣度優先走訪頂點：')#列印廣度優先走訪的頂點
bfs(1)
print()
