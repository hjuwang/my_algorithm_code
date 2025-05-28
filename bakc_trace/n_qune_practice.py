#  n 皇后问题,按行递归,按列循环

# 每一个解答都是一个二维数组，所以需要返回一个三数组
def n_quenes(n: int)-> list[list[list]]:
    # 初始化矩阵
    state = [[0]*n for _ in range(n)]
    # 表示每一列上是否有 皇后
    cols = [False]*n

    # 表示主对角线上是否有皇后
    major_diag = [False] * (2*n-1)
    minor_diag = [False] * (2*n-1)

    # 使用这个数组存储结果
    res = []

    #调用算法函数
    back_track(n,0,cols,major_diag,minor_diag,res,state)
    
    #返回结果
    return res
# 主要的递归算法

def back_track(
    n: int,
    row_index: int, # 在第几行上摆放皇后
    # 下面是三个条件
    cols: list[bool],
    major: list[bool],
    minor: list[bool],

    #存储结果
    res: list[list[list[int]]],

    #当前的状态
    state: list[list[int]]    
) :
    
    # 如果 已经摆放完毕则添加结果，并返回
    if row_index== n:
        res.append([list(row) for row in state])
        return

    #开始尝试(针对每一列)
    for col_index in range(n):
        # 计算其所在的主和次对角线
        major_index = row_index-col_index+n-1
        minor_index = row_index+col_index
        # 如果本元素所在列&所在主对角线&所在次对角线都没有皇后，方可放置
        if not cols[col_index] and not major[major_index] and not minor[minor_index]:
            #放置皇后
            state[row_index][col_index]=1
            #标记
            cols[col_index]=major[major_index]=minor[minor_index]=True
            #尝试下一行
            back_track(n,row_index+1,cols,major,minor,res,state)
            # 回退
            state[row_index][col_index]=0
            #将三个标记还原
            cols[col_index]=major[major_index]=minor[minor_index]=False                        
        
# 执行这个程序
if __name__=="__main__":
    res=n_quenes(4)
    print(res)