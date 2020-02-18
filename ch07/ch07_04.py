class tree:
    def __init__(self):
        self.data=0
        self.left=None
        self.right=None

def create_tree(root,val):  #建立二元樹函數
    newnode=tree()
    newnode.data=val
    newnode.left=None
    newnode.right=None
    if root==None:
        root=newnode
        return root
    else:
        current=root
        while current!=None:
            backup=current
            if current.data > val:
                current=current.left
            else:
                current=current.right
        if backup.data >val:
            backup.left=newnode
        else:
            backup.right=newnode
    return root

def search(ptr,val):     #搜尋二元樹副程式
    i=1
    while True:
        if ptr==None:    #沒找到就傳回None
            return None
        if ptr.data==val:       #節點值等於搜尋值
            print('共搜尋 %3d 次' %i)
            return ptr
        elif ptr.data > val:  #節點值大於搜尋值
            ptr=ptr.left
        else:
            ptr=ptr.right
        i+=1

#主程式
arr=[7,1,4,2,8,13,12,11,15,9,5]
ptr=None
print('[原始陣列內容]')
for i in range(11):
    ptr=create_tree(ptr,arr[i])  #建立二元樹
    print('[%2d] ' %arr[i],end='')
print()
data=int(input('請輸入搜尋值：'))
if search(ptr,data) !=None :  #搜尋二元樹
    print('你要找的值 [%3d] 有找到!!' %data)
else:
    print('您要找的值沒找到!!')
