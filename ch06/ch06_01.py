MAXSTACK=100 #定義最大堆疊容量
global stack
stack=[None]*MAXSTACK  #堆疊的陣列宣告
top=-1 #堆疊的頂端

#判斷是否為空堆疊
def isEmpty():
    if(top==-1):
        return True
    else:
        return False

#將指定的資料存入堆疊
def push(data):
    global top
    global MAXSTACK
    global stack
    if top>=MAXSTACK-1:
        print('堆疊已滿,無法再加入')
    else:
        top +=1
        stack[top]=data #將資料存入堆疊

#從堆疊取出資料*/
def pop():
    global top
    global stack
    if isEmpty():
        print('堆疊是空')
    else:
        print('彈出的元素為: %d' % stack[top])
        top=top-1     
        
#主程式
i=2
count=0
while True:
    i=int(input('要推入堆疊,請輸入1,彈出則輸入0,停止操作則輸入-1: '))
    if i==-1:
        break
    elif i==1:
        value=int(input('請輸入元素值:'))
        push(value)
    elif i==0:
        pop()

print('============================')
if top <0:
    print('\n 堆疊是空的')
else:
    i=top
    while i>=0:
        print('堆壘彈出的順序為:%d' %(stack[i]))
        count +=1
        i =i-1
    print 

print('============================') 
