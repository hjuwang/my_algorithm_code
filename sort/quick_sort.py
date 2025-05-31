#快速排序
#理解快速排序，的关键要点是哨兵划分的思想
#然后递归的调用哨兵划分

def parttion(array,left: int,right:int)->int:
    i,j= left,right
    while i<j:
        # 从左边向右找到第一个大于哨兵元素的元素、
        while i<j and array[i]<=array[right]:
            i+=1
        # 从右边向左找到第一个小于哨兵元素的元素
        while i<j and array[j]>=array[right]:
            j-=1
        #因为和哨兵元素比大小（调换元素的位置）
        array[i],array[j]=array[j],array[i]
    # 将哨兵元素和其中一个边界调换位置,并返回边界索引
    array[i],array[right]=array[right],array[i]
    return i

def quick_sort(array,left:int,right:int):
    if left>=right:
        return
    povit=parttion(array,left,right)
    # 分治策略
    # 这个地方需要注意 
    quick_sort(array,left,povit-1)
    quick_sort(array,povit+1,right)
         

array = [3,5,8,1,2,9,4,7,6]
quick_sort(array,left=0,right=len(array)-1)
print(array)        

# 时间复杂度分析：
# 递归树的深度为logN,每一层需要交换的次数为n 所以时间复杂度是O(N*logN)