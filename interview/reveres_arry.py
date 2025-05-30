
# 给定一个

def hui_array(array:list[int])-> list[int]:
    
    i=0
    origin_len = len(array)
    while i<origin_len:
        # 对称位置的索引
        dui_c_index = -1-i 
        # 相等就没关系
        if array[i]!=array[dui_c_index]:
            # 最后一个位置添加
            if i==0:
                array.append(array[i])
            # 其他位置插入 
            else:
                array.insert(dui_c_index+1,array[i])    
        i+=1
    return array            
def make_palindrome(arr):
    return arr + arr[:-1][::-1]

array=[3, 5, 2, 1]
res1 = hui_array(array=array)
print(res1)
