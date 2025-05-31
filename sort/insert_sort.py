# 插入排序算法
# 将已经排序的范围逐渐扩大,默认第0个元素是已经排序的
# 可以将这个算法想象成插队

def insert_sort(array):
    n = len(array)
    
    # 外层循环
    for  i in range(1,n):
        # 将这个基准数字插入到合适的位置（让第几个人开始插队）
        base = array[i]
        j=i-1
        # 插队的条件是(只要前面的人比我高，我就让他向后挪动一个位置)
        while j >= 0 and array[j]>base:
            # 比base 大的要依次向后移动一个位置
            array[j+1]=array[j]
            j-=1
        
        array[j+1]=base
 
 
array = [7,5,4,8,3,4,9,6,2]

insert_sort(array)

print(array)            

#时间复杂度是O(n*n)的级别
