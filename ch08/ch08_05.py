SIZE=7  
NUMBER=6
INFINITE=99999 # 無窮大  

Graph_Matrix=[[0]*SIZE for row in range(SIZE)] # 圖形陣列
distance=[[0]*SIZE for row in range(SIZE)] # 路徑長度陣列

# 建立圖形 
def BuildGraph_Matrix(Path_Cost):
    for i in range(1,SIZE):
        for j in range(1,SIZE):
            if i == j :
                Graph_Matrix[i][j] = 0 # 對角線設為0
            else:
                Graph_Matrix[i][j] = INFINITE
    # 存入圖形的邊線
    i=0
    while i<SIZE:
        Start_Point = Path_Cost[i][0]
        End_Point = Path_Cost[i][1]
        Graph_Matrix[Start_Point][End_Point]=Path_Cost[i][2]
        i+=1
        
# 印出圖形 
 
def shortestPath(vertex_total):
    # 圖形長度陣列初始化
    for i in range(1,vertex_total+1):
        for j in range(i,vertex_total+1):
            distance[i][j]=Graph_Matrix[i][j]
            distance[j][i]=Graph_Matrix[i][j]

    # 利用Floyd演算法找出所有頂點兩兩之間的最短距離
    for k in range(1,vertex_total+1):
        for i in range(1,vertex_total+1):
            for j in range(1,vertex_total+1):
                if distance[i][k]+distance[k][j]<distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
            

Path_Cost = [[1, 2,20],[2, 3, 30],[2, 4, 25], \
             [3, 5, 28],[4, 5, 32],[4, 6, 95],[5, 6, 67]] 
BuildGraph_Matrix(Path_Cost)
print('===========================================')
print('      所有頂點兩兩之間的最短距離: ')
print('===========================================')
shortestPath(NUMBER) # 計算所有頂點間的最短路徑 
#求得兩兩頂點間的最短路徑長度陣列後，將其印出
print('     頂點1  頂點2  頂點3  頂點4  頂點5  頂點6')
for i in range(1,NUMBER+1):
    print('頂點%d' %i, end='')
    for j in range(1,NUMBER+1):
        print('%5d ' %distance[i][j],end='')
    print()
print('===========================================')
print()
