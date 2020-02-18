# 以for迴圈計算 n! 
sum = 1
n=int(input('請輸入n='))
for i in range(0,n+1):
    for j in range(i,0,-1):
        sum *= j    # sum=sum*j
    print('%d!=%3d' %(i,sum))
    sum=1
