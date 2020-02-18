def hanoi(n, p1, p2, p3):
    if n==1: # 遞迴出口
        print('套環從 %d 移到 %d' %(p1, p3))
    else:
        hanoi(n-1, p1, p3, p2)
        print('套環從 %d 移到 %d' %(p1, p3))
        hanoi(n-1, p2, p1, p3)

j=int(input('請輸入所移動套環數量：'))
hanoi(j,1, 2, 3)
