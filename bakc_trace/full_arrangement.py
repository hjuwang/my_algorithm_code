# 全排列问题的练习

def full_arrangement(
    array: list[int],
    state: list[int],selected:list[bool],
    res: list[list[int]]):
    
        if len(state)==len(array):
            res.append(state.copy())
            return
        #循环尝试数组中的每一个元素
        for index in range(len(array)):
            if not selected[index]:
                state.append(array[index])
                selected[index]=True
                full_arrangement(array,state,selected,res)
                # 回退
                selected[index]=False
                state.pop()