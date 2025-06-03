# 字符串随机组合的问题，共有多少种排列的方式

def back_trace(str_list:list[list[str]],
               str_list_index:int,
               state:list[str],
               res:list[str]):
    if str_list_index ==len(str_list):
        res.append("".join(state.copy()))
        return
    
    for cstr in str_list[str_list_index]:
            #选择一个
            state.append(cstr)
            #继续选择
            back_trace(str_list,str_list_index+1,state,res)
            #回退(尝试本层的其他可能)
            state.pop()
            

res = []
state=[]

str_list= [["ab","c","d"],["e","f"],["op","q","rs"]]

back_trace(str_list,0,state,res)             

print(res)

# 采用回溯的思想解决本题
# 考虑一下这个算法的递归树，并没有递归树，有的只是简单的全排列
# 递归树的深度为n(外层数组的大小)，所以空间复杂度为O(n)线性阶
# 假设内层数组的长度为2 ，每一层的循环次数成指数型增长，所以时间复杂度是O(2^n)指数阶
