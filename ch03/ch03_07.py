# 基數排序法 由小到大排序
import random

def inputarr(data,size):
    for i in range(size):
        data[i]=random.randint(0,999) #設定data值最大為3位數

def showdata(data,size):
    for i in range(size):
        print('%5d' %data[i],end='')
    print()

def radix(data,size): 
     n=1 #n為基數，由個位數開始排序
     while n<=100:
        tmp=[[0]*100 for row in range(10)] # 設定暫存陣列，[0~9位數][資料個數]，所有內容均為0
        for i in range(size): # 比對所有資料
            m=(data[i]//n)%10# m為n位數的值，如 36取十位數 (36/10)%10=3
            tmp[m][i]=data[i]# 把data[i]的值暫存於tmp 裡
        k=0
        for i in range(10):
            for j in range(size):
                if tmp[i][j] != 0:    # 因一開始設定 tmp ={0}，故不為0者即為
                    data[k]=tmp[i][j] # data暫存在 tmp 裡的值，把tmp 裡的值放
                    k+=1              # 回data[ ]裡
        print('經過%3d位數排序後：' %n,end='')
        showdata(data,size)
        n=10*n

def main():
    data=[0]*100
    size=int(input('請輸入陣列大小(100以下)：'))
    print('您輸入的原始資料是：')
    inputarr (data,size)
    showdata (data,size)
    radix (data,size)

main()
