# 给定一个target int,从数组中选择，出两个元素的索引，让这两个元素的和为target

# 以空间换时间
def hash_search(array:list[int],target)->list[int]:
    # 定义一个hash 表 value:index
    dict= {}
    for i in range(len(array)):
        if target -array[i] in dict:
            return [dict[target -array[i]],i]
    # 将array[i]添加到dict
        dict[array[i]]=i
        
    return []



array = [1,2,3,4,5,6,7,8]

res = hash_search(array=array,target=12)    
print(res)

# 通过这个例子顺便学习一下 python 中的字典
'''
字典中的key 必须是相同的类型，但value 不用是相同的类型
删除字典中的元素可以使用 del 内建函数
判断字典中是否存在某个值，可以使用 in 关键字
'''