SIZE=7  
NUMBER=6
INFINITE=99999 # 無窮大  

Graph_Matrix=[[0]*SIZE for row in range(SIZE)] # 圖形陣列
distance=[0]*SIZE  # 路徑長度陣列

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
            

# 單點對全部頂點最短距離  
def shortestPath(vertex1, vertex_total):
    shortest_vertex = 1 #紀錄最短距離的頂點
    goal=[0]*SIZE  #用來紀錄該頂點是否被選取
    for i in range(1,vertex_total+1):
        goal[i] = 0
        distance[i] = Graph_Matrix[vertex1][i]
    goal[vertex1] = 1
    distance[vertex1] = 0
    print()

    for i in range(1,vertex_total):
        shortest_distance = INFINITE
        for j in range(1,vertex_total+1):
            if goal[j]==0 and shortest_distance>distance[j]:
                shortest_distance=distance[j]
                shortest_vertex=j
            
        goal[shortest_vertex] = 1
        # 計算開始頂點到各頂點最短距離 
        for j in range(vertex_total+1):
            if goal[j] == 0 and \
               distance[shortest_vertex]+Graph_Matrix[shortest_vertex][j] \
               <distance[j]:
                distance[j]=distance[shortest_vertex] \
                +Graph_Matrix[shortest_vertex][j]

# 主程式
global Path_Cost
Path_Cost = [ [1, 2, 29], [2, 3, 30],[2, 4, 35], \
              [3, 5, 28],[3, 6, 87],[4, 5, 42], \
              [4, 6, 75],[5, 6, 97]]

BuildGraph_Matrix(Path_Cost)
shortestPath(1,NUMBER) # 找尋最短路徑 
print('-----------------------------------')
print('頂點1到各頂點最短距離的最終結果')
print('-----------------------------------')
for j in range(1,SIZE):
    print('頂點 1到頂點%2d的最短距離=%3d' %(j,distance[j]))
print('-----------------------------------')
print()
