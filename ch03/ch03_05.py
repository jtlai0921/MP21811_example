# 合併排序法(Merge Sort)

#99999為串列1的結束數字不列入排序
list1 = [20,45,51,88,99999]
#99999為串列2的結束數字不列入排序
list2 = [98,10,23,15,99999] 
list3 = []

def merge_sort():
    global list1
    global list2
    global list3
        
    # 先使用選擇排序將兩數列排序，再作合併
    select_sort(list1, len(list1)-1)
    select_sort(list2, len(list2)-1)

    
    print('\n第1組資料的排序結果: ', end = '')
    for i in range(len(list1)-1):
        print(list1[i], ' ', end = '')

    print('\n第2組資料的排序結果: ', end = '')
    for i in range(len(list2)-1):
        print(list2[i], ' ', end = '')
    print()

    for i in range(60):
        print('=', end = '')
    print()

    My_Merge(len(list1)-1, len(list2)-1)

    for i in range(60):
        print('=', end = '')
    print()

    print('\n合併排序法的最終結果: ', end = '')
    for i in range(len(list1)+len(list2)-2):
        print('%d ' % list3[i], end = '')
        
def select_sort(data, size):
    for base in range(size-1):
        small = base
        for j in range(base+1, size):
            if data[j] < data[small]:
                small = j
        data[small], data[base] = data[base], data[small]

def My_Merge(size1, size2):
    global list1
    global list2
    global list3

    index1 = 0
    index2 = 0
    for index3 in range(len(list1)+len(list2)-2):
        if list1[index1] < list2[index2]: # 比較兩數列，資料小的先存於合併後的數列
            list3.append(list1[index1])
            index1 += 1
            print('此數字%d取自於第1組資料' % list3[index3])
        else:
            list3.append(list2[index2])
            index2 += 1
            print('此數字%d取自於第2組資料' % list3[index3])
        print('目前的合併排序結果: ', end = '')
        for i in range(index3+1):
            print(list3[i], ' ', end = '')
        print('\n')

#主程式開始

merge_sort()  #呼叫所定義的合併排序法函數
