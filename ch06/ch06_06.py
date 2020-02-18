class student:
    def __init__(self):
        self.name=' '*20
        self.score=0
        self.next=None
        
front=student()
rear=student()
front=None
rear=None

def enqueue(name, score):  # 置入佇列資料
    global front
    global rear
    new_data=student()  # 配置記憶體給新元素
    new_data.name=name  # 設定新元素的資料
    new_data.score = score
    if rear==None: # 如果rear為None，表示這是第一個元素
        front = new_data
    else:
        rear.next = new_data    # 將新元素連接至佇列尾端

    rear = new_data    # 將rear指向新元素，這是新的佇列尾端
    new_data.next = None    # 新元素之後無其它元素

def dequeue(): # 取出佇列資料
    global front
    global rear
    if front == None:
        print('佇列已空！')
    else:
        print('姓名：%s\t成績：%d ....取出' %(front.name, front.score))
        front = front.next    # 將佇列前端移至下一個元素
        
def show():     # 顯示佇列資料
    global front
    global rear
    ptr = front
    if ptr == None:
        print('佇列已空！')
    else:
        while ptr !=None: # 由front往rear走訪佇列
            print('姓名：%s\t成績：%d' %(ptr.name, ptr.score))
            ptr = ptr.next

select=0
while True:
    select=int(input('(1)存入 (2)取出 (3)顯示 (4)離開 => '))
    if select==4:
        break
    if select==1:
        name=input('姓名: ')
        score=int(input('成績: '))
        enqueue(name, score)
    elif select==2:
        dequeue()
    else:
        show()
