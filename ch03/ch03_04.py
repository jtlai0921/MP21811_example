SIZE=8

def showdata(data):
    for i in range(SIZE):
        print('%3d' %data[i],end='')
    print()

def shell(data,size):
    k=1 #k列印計數
    jmp=size//2
    while jmp != 0:
        for i in range(jmp, size):  #i為掃描次數 jmp為設定間距位移量
            tmp=data[i] #tmp用來暫存資料
            j=i-jmp  #以j來定位比較的元素
            while tmp<data[j] and j>=0:  #插入排序法
                data[j+jmp] = data[j]
                j=j-jmp
            data[jmp+j]=tmp
        print('第 %d 次排序過程：' %k,end='')  
        k+=1
        showdata (data)
        print('-----------------------------------------')
        jmp=jmp//2    #控制迴圈數

def main():
    data=[16,25,39,27,12,8,45,63]
    print('原始陣列是：     ')	
    showdata (data)
    print('-----------------------------------------')
    shell(data,SIZE)

main()
