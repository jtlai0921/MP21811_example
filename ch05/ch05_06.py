#include <stdio.h>
#include <stdlib.h>
class employee:
    def __init__(self):
        self.num=0
        self.salary=0
        self.name=''
        self.next=None

findword=0

namedata=['Allen','Scott','Marry','Jon', \
          'Mark','Ricky','Lisa','Jasica', \
          'Hanson','Amy','Bob','Jack']

data=[[1001,32367],[1002,24388],[1003,27556],[1007,31299], \
      [1012,42660],[1014,25676],[1018,44145],[1043,52182], \
      [1031,32769],[1037,21100],[1041,32196],[1046,25776]]

head=employee() #建立串列首
if not head:
    print('Error!! 記憶體配置失敗!!')
    sys.exit(0)

head.num=data[0][0]
head.name=namedata[0]
head.salary=data[0][1]
head.next=None
ptr=head
for i in range(1,12): #建立鏈結串列
    newnode=employee()
    newnode.num=data[i][0]
    newnode.name=namedata[i]
    newnode.salary=data[i][1]
    newnode.next=None
    ptr.next=newnode
    ptr=ptr.next

ptr=head
i=0
print('原始員工串列節點資料：')
while ptr !=None:  #列印串列資料
    print('[%2d %6s %3d] => ' %(ptr.num,ptr.name,ptr.salary), end='')
    i=i+1
    if i>=3: #三個元素為一列
        print()
        i=0
    ptr=ptr.next

ptr=head
before=None   
print('\n反轉後串列節點資料：')
while ptr!=None: #串列反轉,利用三個指標
    last=before
    before=ptr
    ptr=ptr.next
    before.next=last

ptr=before
while ptr!=None:
    print('[%2d %6s %3d] => ' %(ptr.num,ptr.name,ptr.salary), end='')
    i=i+1
    if i>=3:
        print()
        i=0
    ptr=ptr.next
