import sys

MAX=10			#定義佇列的大小
queue=[0]*MAX
front=rear=-1
choice=''
while rear<MAX-1 and choice !='e':
    choice=input('[a]表示存入一個數值[d]表示取出一個數值[e]表示跳出此程式: ')
    if choice=='a':
        val=int(input('[請輸入數值]: '))
        rear+=1
        queue[rear]=val
    elif choice=='d':
        if rear>front:
            front+=1
            print('[取出數值為]: [%d]' %(queue[front]))
            queue[front]=0
        else:
            print('[佇列已經空了]')
            sys.exit(0)
    else:
        print()

print('------------------------------------------')
print('[輸出佇列中的所有元素]:')

if rear==MAX-1:
    print('[佇列已滿]')
elif front>=rear:
    print('沒有')
    print('[佇列已空]')
else:
    while rear>front:
        front+=1
        print('[%d] ' %queue[front],end='')
    print()
    print('------------------------------------------')
print()
