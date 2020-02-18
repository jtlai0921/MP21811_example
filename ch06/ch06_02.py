class Node:  #堆疊鏈結節點的宣告
    def __init__(self):
        self.data=0  #堆疊資料的宣告
        self.next=None  #堆疊中用來指向下一個節點

top=None

def isEmpty():
    global top
    if(top==None):
        return 1
    else:
        return 0
    
#將指定的資料存入堆疊
def push(data):
    global top
    new_add_node=Node()
    new_add_node.data=data#將傳入的值指定為節點的內容
    new_add_node.next=top#將新節點指向堆疊的頂端
    top=new_add_node#新節點成為堆疊的頂端


#從堆疊取出資料
def pop():
    global top
    if isEmpty():
        print('===目前為空堆疊===')
        return -1
    else:
        ptr=top#指向堆疊的頂端
        top=top.next#將堆疊頂端的指標指向下一個節點
        temp=ptr.data#取出堆疊的資料
        return temp#將從堆疊取出的資料回傳給主程式
        
#主程式
while True:
    i=int(input('要推入堆疊,請輸入1,彈出則輸入0,停止操作則輸入-1: '))
    if i==-1:
        break
    elif i==1:
        value=int(input('請輸入元素值:')) 
        push(value)
    elif i==0:
        print('彈出的元素為%d' %pop())
    
print('============================')
while(not isEmpty()): #將資料陸續從頂端彈出
    print('堆疊彈出的順序為:%d' %pop()) 
print('============================')
