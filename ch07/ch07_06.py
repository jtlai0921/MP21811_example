def heap(data,size):
    for i in range(int(size/2),0,-1):#建立堆積樹節點
        ad_heap(data,i,size-1)
    print()
    print('堆積內容：',end='')
    for i in range(1,size): #原始堆積樹內容
        print('[%2d] ' %data[i],end='')
    print('\n')
    for i in range(size-2,0,-1): #堆積排序
        data[i+1],data[1]=data[1],data[i+1]#頭尾節點交換
        ad_heap(data,1,i)#處理剩餘節點
        print('處理過程：',end='')
        for j in range(1,size):
            print('[%2d] ' %data[j],end='')
        print()

def ad_heap(data,i,size):
    j=2*i
    tmp=data[i]
    post=0
    while j<=size and post==0:
        if j<size:
            if data[j]<data[j+1]: #找出最大節點
                j+=1
        if tmp>=data[j]: #若樹根較大，結束比較過程
            post=1
        else:
            data[int(j/2)]=data[j]#若樹根較小，則繼續比較
            j=2*j
    data[int(j/2)]=tmp #指定樹根為父節點

def main():
    data=[0,5,6,4,8,3,2,7,1]	#原始陣列內容
    size=9
    print('原始陣列：',end='')
    for i in range(1,size):
        print('[%2d] ' %data[i],end='')
    heap(data,size) #建立堆積樹
    print('排序結果：',end='')
    for i in range(1,size):
        print('[%2d] ' %data[i],end='')
        
main()
