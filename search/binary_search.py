# 最简单的二分查找，数组是已经排序的数组
'''
在区间[0,n-1]查找
定义双指针 i,j=0,n-1
m = i+(j-i)/2
如果 target<array[m],则区间变化为[i,m]
如果 target>array[m],则区间变化为[m+1,j]

'''
# 返回target 的索引
def binary_search(array:list[int],target: int)->int:
    i,j = 0,len(array)-1
   
    while i<=j:
        mid = i+((j-i)//2)
        if target<array[mid]:
            j=mid-1
        elif target>array[mid]:
            i=mid+1                                                                                                                                                                    
        else:
            return mid
    return -1


array = [1,2,3,4,5,6,7,8,9,10]

res= binary_search(array,5) 

print(res)           