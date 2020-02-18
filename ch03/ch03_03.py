SIZE=8        #定義陣列大小
def showdata(data):
    for i in range(SIZE):
        print('%3d' %data[i],end='')   #列印陣列資料
    print()
    
def insert(data):
    for i in range(1,SIZE):
        tmp=data[i] #tmp用來暫存資料
        no=i-1
        while no>=0 and tmp<data[no]:
            data[no+1]=data[no]	#就把所有元素往後推一個位置
            no-=1
        data[no+1]=tmp #最小的元素放到第一個元素

def main():
    data=[16,25,39,27,12,8,45,63]
    print('原始陣列是：')
    showdata(data)
    insert(data)
    print('排序後陣列是：')
    showdata(data)

main()
