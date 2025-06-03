# 使用一个新数组来统计 待排序索引的数组中每个数字出现的个数，
# 新数组的索引作为待排序的元素

def counter_sort(array:list[int]):
    max_v = max(array)
    counter= [0]*(max_v+1)
    # 统计每个数字出现的次数
    for v in array:
        counter[v]+=1
    
    #回填到原来的数组,从后
    i=0
    for count_index in range(len(counter)):
        # 回填到原来的数组中
        # 把count_index 填写 counter[count_index] 次
        for _ in range(counter[count_index]):
            array[i]=count_index
            i+=1
        
array = [7,5,4,8,3,4,9,6,2]

counter_sort(array) 

print(array)     


# 时间复杂度分析 ：
'''
遍历原数组的时间复杂度为n
假设counter 的长度为m，外层循环为m,每一次的内层循环的范围是[0,n],建设为一个常数k(说明每一个元素出现的次数都很平均)
所以时间复杂度为O(n+m*k)约等于 o(n)

'''  
    
    