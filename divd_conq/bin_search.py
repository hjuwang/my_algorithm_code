# 基于分支思想的二分查找
# 首先数组是一个排序的数组
# 记查找在范围[i,j]中寻找target 的函数为f(i,j)
# mid = (i+j)//2
# 如果 array[mid]<target,说明在右半部分，则问题的解又可以看成f(mid+1,j)
# 如果 array[mid]>target,说明在左半部分，则问题的解又可以看成f(i,mid-1)

def bin_search(array:list[int],target:int,i:int,j:int)->int:
    # 说明没找到(边界问题)
    if i>j:
        return -1
    mid = (i+j)//2
    if array[mid]<target:
        i=mid+1
        return bin_search(array,target,i,j)
    elif array[mid]>target:
        j=mid-1
        return bin_search(array,target,i,j)
    else:
        return mid
    

array = [1,2,3,4,5,6,7,8,9]
i,j=0,len(array)-1
res =bin_search(array,9,i,j)
print(res)    
            
