VERTS=6                #圖形頂點數

class edge:  #邊的組成宣告
    def __init__(self):
        self.start=0
        self.to=0
        self.find=0
        self.val=0
        self.next=None

v=[0]*(VERTS+1)   


def findmincost(head):  #搜尋成本最小的邊
    minval=100
    ptr=head
    while ptr!=None:
        if ptr.val<minval and ptr.find==0: #假如ptr.val的值小於minval
            minval=ptr.val                 #就把ptr.val設為最小值
            retptr=ptr                     #並且把ptr紀錄下來
        ptr=ptr.next
    retptr.find=1  #將retptr設為已找到的邊
    return retptr  #傳回retptr
        

def mintree(head):                    #最小成本擴張樹函數
    global VERTS
    result=0
    ptr=head
    for i in range(VERTS):
        v[i]=0
    while ptr!=None:
        mceptr=findmincost(head)
        v[mceptr.start]=v[mceptr.start]+1
        v[mceptr.to]=v[mceptr.to]+1
        if v[mceptr.start]>1 and v[mceptr.to]>1:
            v[mceptr.start]=v[mceptr.start]-1
            v[mceptr.to]=v[mceptr.to]-1
            result=1
        else:
            result=0
        if result==0:
            print('起始頂點 [%d] -> 終止頂點 [%d] -> 路徑長度 [%d]' \
                  %(mceptr.start,mceptr.to,mceptr.val))
        ptr=ptr.next
            
#成本表陣列
data=[[1,2,6],[1,6,12],[1,5,10],[2,3,3], \
      [2,4,5],[2,6,8],[3,4,7],[4,6,11], \
      [4,5,9],[5,6,16]]
head=None
#建立圖形串列
for i in range(10):
    for j in range(1,VERTS+1):
        if data[i][0]==j:
            newnode=edge()
            newnode.start=data[i][0]
            newnode.to=data[i][1]
            newnode.val=data[i][2]
            newnode.find=0
            newnode.next=None
            if head==None:
                head=newnode
                head.next=None
                ptr=head
            else:
                ptr.next=newnode
                ptr=ptr.next
            
print('-------------------------------------------------')
print('建立最小成本擴張樹：')
print('-------------------------------------------------')
mintree(head)                        #建立最小成本擴張樹
