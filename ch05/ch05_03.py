arrA=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
N=4
#宣告4x4陣列arr
arrB=[[None] * N for row in range(N)]

print('[原設定的矩陣內容]')
for i in range(4):
    for j in range(4):
        print('%d' %arrA[i][j],end='\t')
    print()

#進行矩陣轉置的動作
for i in range(4):
    for j in range(4):
        arrB[i][j]=arrA[j][i]
	
print('[轉置矩陣的內容為]')
for i in range(4):
    for j in range(4):
        print('%d' %arrB[i][j],end='\t')
    print()
