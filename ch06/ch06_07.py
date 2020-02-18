class Node:
    def __init__(self):
        self.data=0
        self.next=None
        
front=Node()
rear=Node()
front=None
rear=None

#方法enqueue:佇列資料的存入
def enqueue(value):
    global front
    global rear
    node=Node()  #建立節點
    node.data=value
    node.next=None
    #檢查是否為空佇列
    if rear==None:
        front=node #新建立的節點成為第1個節點
    else:
        rear.next=node#將節點加入到佇列的尾端
    rear=node#將佇列的尾端指標指向新加入的節點

#方法dequeue:佇列資料的取出
def dequeue(action):
    global front
    global rear
    #從前端取出資料
    if not(front==None) and action==1:
        if front==rear:
            rear=None
        value=front.data#將佇列資料從前端取出
        front=front.next#將佇列的前端指標指向下一個
        return value
    #從尾端取出資料
    elif not(rear==None) and action==2:
        startNode=front#先記下前端的指標值
        value=rear.data#取出目前尾端的資料
        #找尋最尾端節點的前一個節點
        tempNode=front
        while front.next!=rear and front.next!=None:
            front=front.next
            tempNode=front
        front=startNode#記錄從尾端取出資料後的佇列前端指標
        rear=tempNode#記錄從尾端取出資料後的佇列尾端指標
        #下一行程式是指當佇列中僅剩下最節點時,
        #取出資料後便將front及rear指向None
        if front.next==None or rear.next==None:
            front=None
            rear=None
        return value
    else:
        return -1
    
print('以鏈結串列來實作雙向佇列')
print('====================================')

ch='a'
while True:
    ch=input('加入請按 a,取出請按 d,結束請按 e:')
    if ch =='e':
        break
    elif ch=='a':
        item=int(input('加入的元素值:'))
        enqueue(item)
    elif ch=='d':
        temp=dequeue(1)
        print('從雙向佇列前端依序取出的元素資料值為：%d' %temp)
        temp=dequeue(2)
        print('從雙向佇列尾端依序取出的元素資料值為：%d' %temp)
    else:
        break
