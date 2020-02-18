import sys
class employee:
    def __init__(self):
        self.num=0
        self.salary=0
        self.name=''
        self.next=None
        
def del_ptr(head,ptr):  #刪除節點副程式
    top=head
    if ptr.num==head.num:  #[情形1]:刪除點在串列首
        head=head.num
        print('已刪除第 %d 號員工 姓名：%s 薪資:%d' %(ptr.num,ptr.name,ptr.salary))
    else:
        while top.next!=ptr:  #找到刪除點的前一個位置
            top=top.next
        if ptr.next==None:   #刪除在串列尾的節點
            top.next=None
            print('已刪除第 %d 號員工 姓名：%s 薪資:%d' %(ptr.num,ptr.name,ptr.salary))
        else:
            top.next=ptr.next #刪除在串列中的任一節點
            print('已刪除第 %d 號員工 姓名：%s 薪資:%d' %(ptr.num,ptr.name,ptr.salary))
    return head  #回傳串列

def main():
    findword=0
    namedata=['Allen','Scott','Marry','John',\
              'Mark','Ricky','Lisa','Jasica',\
              'Hanson','Amy','Bob','Jack']
    data=[[1001,32367],[1002,24388],[1003,27556],[1007,31299], \
          [1012,42660],[1014,25676],[1018,44145],[1043,52182], \
          [1031,32769],[1037,21100],[1041,32196],[1046,25776]]
    print('員工編號 薪水 員工編號 薪水 員工編號 薪水 員工編號 薪水')
    print('-------------------------------------------------------')
    for i in range(3):
        for j in range(4):
            print('%2d  [%3d]  ' %(data[j*3+i][0],data[j*3+i][1]),end='')
        print()
    head=employee() #建立串列首
    if not head:
        print('Error!! 記憶體配置失敗!!')
        sys.exit(0)
    head.num=data[0][0]
    head.name=namedata[0]
    head.salary=data[0][1]
    head.next=None
	
    ptr=head
    for i in range(1,12):  #建立串列
        newnode=employee()
        newnode.num=data[i][0]
        newnode.name=namedata[i]
        newnode.salary=data[i][1]
        newnode.num=data[i][0]
        newnode.next=None
        ptr.next=newnode
        ptr=ptr.next
			
    while(True):
        findword=int(input('請輸入要刪除的員工編號,要結束刪除過程,請輸入-1：'))
        if(findword==-1): #迴圈中斷條件
            break
        else:
            ptr=head
            find=0
            while ptr!=None:
                if ptr.num==findword:
                    ptr=del_ptr(head,ptr)
                    find=find+1
                    head=ptr
                ptr=ptr.next
            if find==0:
                print('######沒有找到######')
			
    ptr=head
    print('\t座號\t    姓名\t成績')   #列印剩餘串列資料
    print('\t==============================')
    while(ptr!=None):
        print('\t[%2d]\t[ %-10s]\t[%3d]' %(ptr.num,ptr.name,ptr.salary))
        ptr=ptr.next
main()
