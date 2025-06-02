# 归并排序，先拆分，后合并，拆分简单，关键在合并
# 


def meger_sort(array:list[int])->list[int]:

   #递归出口  
    if len(array)==1:
        return array
    #拆分
    mid =len(array)//2
    #递归执行拆分后的数组
    left_sort = meger_sort(array=array[:mid])
    right_sort= meger_sort(array=array[mid:])
    # 合并拆分后的数组并返回 
    # return merge_array(left=left_sort,right=right_sort)
    return merger_by_python(left=left_sort,right=right_sort)
     
     

def merge_array(left:list[int],right:list[int])->list[int]:
    # 这里最好还是自己实现一下这排序算法
    
    left_n = len(left)
    right_n= len(right)
    new_array = [0]*(left_n+right_n)
    i,j,k= 0,0,0
    while i<left_n and j<right_n:
        if left[i]<right[j]:
            new_array[k]=left[i]
            i+=1
        else:
            new_array[k]=right[j]
            j+=1
        k+=1
    
    #判断谁剩余
    if i<left_n:
        for i in range(i,left_n):
            new_array[k]=left[i]
            k+=1
    elif j<right_n:
         for j in range(j,right_n):
            new_array[k]=right[j]
            k+=1
    
    return new_array                     
     
     

def merger_by_python(left,right)->list[int]:
    new_array= []
    new_array.extend(left)
    new_array.extend(right)
    sort1 =new_array.sort
    sort1()
    return new_array

# 
array = [6,4,3,7,5,1,2]

sort = meger_sort(array=array)
print(sort)     
 
# array1= [6]
# array2=[5]
# print(merger_by_python(left=array1,right=array2))     