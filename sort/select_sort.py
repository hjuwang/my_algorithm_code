#选择排序算法,长度为n的数组排序
#每次从[i,n-1]范围的数组中选择最小的放在array[i]
# 选择的方式是在这个范围中发现比这个小的就与他换位置
#i的曲直范围是[0,n-2]


def select_sort(array):
    n=len(array)
    for i in range(n-1):
        # 定义一个最小值
        min= array[i]
        for j in range(i+1,n):
            if array[j]<min:
                array[i],array[j]=array[j],array[i]
                
   
   
array = [4,2,7,89,4]

select_sort(array)
print(array)


#时间复杂度分析：
'''
外层循环n-1次，内层循环每次-1，时间复杂度是等比数列 n项目 和 所以是 O(n*n)

常见的场景有 扑克牌 排序
'''
                
        